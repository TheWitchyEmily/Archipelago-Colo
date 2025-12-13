import json, os
from random import Random

import Utils

from CommonClient import logger

from gclib.gcm import GCM
from .Helpers import StringByteFunction as sbf
from .client.constants import CLIENT_VERSION, AP_WORLD_VERSION_NAME

class ColosseumRandomizer:
    def __init__(self, iso_path: str, randomized_output_file_path: str, ap_output_data: bytes, debug_flag=False):
        # Notes randomized folder path and if files should be exported instead of making an ISO
        self.debug = debug_flag
        self.clean_iso_path = iso_path
        self.randomized_output_file_path = randomized_output_file_path

        try:
            if os.path.isfile(randomized_output_file_path):
                tmp_file = open(randomized_output_file_path, "r+")
                tmp_file.close()
        except IOError:
            raise Exception("'" + randomized_output_file_path + "' is currently in use by another application.")

        self.output_data = json.loads(ap_output_data.decode('utf-8'))

        # Server and client version need to match before continuing
        self._check_versions(self.output_data)

        # Read entire ISO contents into memory
        self.gcm = GCM(self.clean_iso_path)
        self.gcm.read_entire_disc()

        # Set random seed
        self.random = Random()
        local_seed: str = str(self.output_data["Seed"])
        self.random.seed(local_seed)

        # Game ID change for save files to be different
        logger.info("Update ISO game ID with AP generated seed")
        bin_data = self.gcm.read_file_data("sys/boot.bin")
        bin_data.seek(0x01)
        bin_data.write(sbf.string_to_bytes(local_seed, len(local_seed))
        self.gcm.changed_files["sys/boot.bin"] = bin_data

        # Handle rest of game randomization/AP related modifications to files

        # Saves randomized iso file, with files updated
        self.save_randomized_iso()

    def _check_versions(self, output_data):
        """
        Compares patch version with client's version
        
        :param output_data: The patch's output data where we attempt to aquire the generated version.
        """
        ap_world_version="<0.1.0"

        if AP_WORLD_VERSION_NAME in output_data:
            ap_world_version = output_data[AP_WORLD_VERSION_NAME]
        if ap_world_version != CLIENT_VERSION:
            raise Utils.VersionException("Error! Server was generated with a different Pokemon Colosseum " +
                        f"APWorld Version.\nThe client version is {CLIENT_VERSION}, which is incompatable with the given version of {ap_world_version}.")

        def save_randomized_isoo(self):
            for _, _ in self.export_files_from_memory():
                continue

    def export_files_from_memory(self):
        yield from self.gcm.export_disc_to_iso_with_changed_files(self.randomized_output_file_path)

if __name__ == '__main__'
    print("Run this from Launcher.py instead")
