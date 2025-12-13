# Heavily based off of Luigi's Mansion lm_rom.py file

from worlds.Files import APPatch, APPlayerContainer, AutoPatchRegister
from settings import get_settings, Settings
from NetUtils import convert_to_base_types
import Utils

from hashlib import md5
from typing import Any
import json, logging, sys, os, zipfile, tempfile

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
        super(ColoUSAPPatch, self).__init__(*args, **kwargs)

    def __get_archive_name(self) -> str:
        if not (Utils.is_windows):
            message = f"Your OS is not supported with this randomizer {sys.platform}."
            logger.error(message)
            raise RuntimeError(message)

        lib_path = ""
        if Utils.is_windows:
            lib_path = "lib-windows"

        logger.info(f"Dependency archive name to use: {lib_path}")
        return lib_path

    def __tmp_folder_name(self) -> str:
        temp_path = os.path.join(tempfile.gettempdir(), "pokemon_colosseum", "libs")
        return temp_path

    def patch(self, apcolo_patch: str) -> str:
        # Get AP path for base rom
        colo_clean_iso = self.get_base_rom_path()
        logger.info(f"Provided Pokemon Colosum ISO Path was: {colo_clean_iso}")
        print("test")

        base_path = os.path.splittext(apcolo_patch)[0]
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

    @classmethod
    def get_base_rom_path(cls) -> str:
        options: Settings = get_settings()
        file_name = options["pokemoncolosseum_options"]["iso_file"]
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
        md5_conv = int(base_md5.hexdiagest(), 16)
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

    def create_iso(self, tmp_dir_path: str, patch_file_path: str, output_iso_path: str, vanilla_iso_patch: str):
        raise Exception("Remote dependencies are currently not possible, generation has failed.")

    def __get_remote_dependencies_and_create_iso(self, appc_patch: str, output_file: str, pc_clean_iso: str):
        raise Exception("Remote dependencies are currently not possible, generation has failed.")
