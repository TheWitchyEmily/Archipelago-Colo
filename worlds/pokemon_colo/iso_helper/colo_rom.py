# Heavily based off of Luigi's Mansion lm_rom.py file

import shutil

from worlds.Files import APPatch, APPlayerContainer, AutoPatchRegister
from settings import get_settings, Settings
from NetUtils import convert_to_base_types
import Utils

from hashlib import md5
from typing import Any
import json, logging, sys, os, zipfile, tempfile
import urllib.request

logger = logging.getLogger()
MAIN_PKG = "worlds.poke_colo.ColossumGenerator"

RANOMIZER_NAME = "Pokemon Colosseum"
COLO_USA_MD5 = 0xe3f389dc5662b9f941769e370195ec90

class InvalidCleanIsoError(Exception):
    """
    Exception raised when there is an issue with the Pokemon Colosseum ISO
    
    Attributes:
        message -- Explain error
    """

    def __init__(self, message="Invalid ISO provided"):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"InvalidCleanIsoError: {self.message}"

class ColoPlayerContainer(APPlayerContainer):
    game = RANOMIZER_NAME
    compression_method = zipfile.ZIP_DEFLATED
    patch_file_ending = ".apcolo"

    def __init__(self, player_choices: dict, patch_path: str, player_name: str, player: int, server: str = ""):
        self.output_data = player_choices
        super().__init__(patch_path, player, player_name, server)

    def write_contents(self, opened_zipfile: zipfile.ZipFile) -> None:
        opened_zipfile.writestr("patch.apcolo", json.dumps(self.output_data, indent=4, default=convert_to_base_types))
        super().write_contents(opened_zipfile)

class PCUSAPPatch(APPatch, metaclass=AutoPatchRegister):
    game = RANOMIZER_NAME
    hash = COLO_USA_MD5
    patch_file_ending = ".apcolo"
    result_file_ending = ".iso"

    procedure = ["custom"]

    def __init__(self, *args: Any, **kwargs: Any):
        super(PCUSAPPatch, self).__init__(*args, **kwargs)

    def __get_archive_name(self) -> str:
        if not (Utils.is_linux or Utils.is_windows):
            message = f"Your OS is not supported with this randomizer {sys.platform}."
            logger.error(message)
            raise RuntimeError(message)

        lib_path = ""
        if Utils.is_windows:
            lib_path = "lib-windows"
        elif Utils.is_linux:
            lib_path = "lib-linux:"

        logger.info(f"Dependency archive name to use: {lib_path}")
        return lib_path

    def __tmp_folder_name(self) -> str:
        temp_path = os.path.join(tempfile.gettempdir(), "pokemon_colosseum", "libs")
        return temp_path

    def patch(self, apcolo_patch: str) -> str:
        # Get AP path for base rom
        colo_clean_iso = self.get_base_rom_path()
        logger.info(f"Provided Pokemon Colosum ISO Path was: {colo_clean_iso}")

        base_path = os.path.splitext(apcolo_patch)[0]
        output_file = base_path + self.result_file_ending

        try:
            # Verify a clean ROM first
            self.verify_base_rom(colo_clean_iso)

            # Use our randomize function to patch the file into an ISO
            from ..PCGenerator import ColosseumRandomizer
            with zipfile.ZipFile(apcolo_patch, "r") as zf:
                appc_bytes = zf.read("patch.apcolo")
            ColosseumRandomizer(colo_clean_iso, output_file, appc_bytes)
        except ImportError:
            self.__get_remote_dependencies_and_create_iso(apcolo_patch, output_file, colo_clean_iso)
        return output_file

    def read_contents(self, appc_patch: str) -> dict[str, Any]:
        with zipfile.ZipFile(appc_patch, "r") as zf:
            with zf.open("archipelago.json", "r") as f:
                manifest = json.load(f)
        if manifest["compatible_version"] > self.version:
            raise Exception(f"File (version: {manifest['compatible_version']} too new "
                f"for this handler (version: {self.version})")
        return manifest

    @classmethod
    def get_base_rom_path(cls) -> str:
        options: Settings = get_settings()
        logger.info(get_settings())
        file_name = options["pokemon_colo_options"]["iso_file"]
        if not os.path.exists(file_name):
            file_name = Utils.user_path(file_name)
        return file_name

    @classmethod
    def verify_base_rom(cls, colo_rom_path: str):
        logger.info("Verifying if provided ISO is valid for a Colosseum USA Edition iso")
        logger.info("Checking GCLib")
        from gclib import fs_helpers as fs
        logger.info("Using GCLib from path: %s.", fs.__file__)

        base_md5 = md5()
        with open(colo_rom_path, "rb") as f:
            while chunk := f.read(1024 * 1024):
                base_md5.update(chunk)

            # Grab Magic Code and Game_ID
            magic = fs.try_read_str(f, 0, 4)
            game_id = fs.try_read_str(f, 0, 6)
            logger.info(f"Magic Code: {magic}")
            logger.info(f"Game ID: {game_id}")

        # Verify file is the right file to load
        md5_conv = int(base_md5.hexdigest(), 16)
        if md5_conv != COLO_USA_MD5:
            raise InvalidCleanISOError(f"Invalid vanilla {RANDOMIZER_NAME} ISO.\nYour ISO may be corrupted or your " +
                "MD5 hashes do not match.\nCorrect ISO hash: {COLO_USA_MD5:x}\nYour ISO's hash: {md5_conv}")

        # Verify provided ISO is valid ISO with valid Game ID
        if magic == "CISO":
            raise InvalidCleanIsoError(f"The provided ISO is in CISO format. {RANOMIZER_NAME} randomizer only supports ISOs in ISO format.")

        if game_id != "GC6E01":
            if game_id and game_id.startswith("GC6"):
                raise InvalidCleanIsoError(f"Invalid version of {RANOMIZER_NAME}. Currently, only the North American version is supported.")
            else:
                raise InvalidCleanIsoError(f"Invalid game given as the vanilla ISO. You must specify a {RANOMIZER_NAME}'s ISO (North American Version).")
        return

    def download_lib_zip(self, tmp_dir_path: str) -> None:
        logger.info("Getting missing dependencies for Pokemon Colosseum from remote source")

        from ..PCClient import CLIENT_VERSION
        lib_path = self.__get_archive_name()
        version_old = "V0.5.8"
        # Use Luigi's Mansion's artifacts for now until our own are uploaded
        lib_path_base = f"https://github.com/BootsinSoots/Archipelago/releases/download/{version_old}"
        download_path = f"{lib_path_base}/{lib_path}.zip"

        tmp_zip_path = os.path.join(tmp_dir_path, "temp.zip")
        with urllib.request.urlopen(download_path) as response, open(tmp_zip_path, 'wb') as created_zip:
            created_zip.write(response.read())

        with zipfile.ZipFile(tmp_zip_path) as z:
            z.extractall(tmp_dir_path)
        return

    def create_iso(self, tmp_dir_path: str, patch_file_path: str, output_iso_path: str, vanilla_iso_path: str):
        logger.info(f"Appending the following to sys path to get dependencies correctly: {tmp_dir_path}")
        sys.path.insert(0, tmp_dir_path)

        # Verify a clean rom
        self.verify_base_rom(vanilla_iso_path)

        # Use custom randomize function to patch ISO
        from ..PCGenerator import ColosseumRandomizer
        with zipfile.ZipFile(patch_file_path, "r") as zf:
            appc_bytes = zf.read("patch.apcolo")
        ColosseumRandomizer(vanilla_iso_path, output_iso_path, appc_bytes)

    def __get_remote_dependencies_and_create_iso(self, appc_patch: str, output_file: str, pc_clean_iso: str):
        try:
            local_dir_path = self.__tmp_folder_name()
            if os.path.isdir(local_dir_path):
                logger.info("Found temp directory after unsuccessful attempt of generating seed, deleting %s.", local_dir_path)
                shutil.rmtree(local_dir_path)
            os.makedirs(local_dir_path, exist_ok=True)
            logger.info("Temp directory created as: %s", local_dir_path)
            self.download_lib_zip(local_dir_path)
            self.create_iso(local_dir_path, appc_patch, output_file, pc_clean_iso)
        except PermissionError:
            logger.warning("Failed to cleanup tmp folder, %s ignoring delete.", local_dir_path)
