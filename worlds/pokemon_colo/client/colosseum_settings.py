import settings

class EmulatorExecutable(settings.UserFilePath):
    """
    Emulator executable path. Automatically starts ROM upon patching completeion.
    If using Flatpak, specify the path here.
    """
    is_exe = True
    description = "The path for emulator executable. If using Flatpak specify this path instad."

class EmulatorAdditionalArguments(list[str]):
    """ Additional arguments to be passed in when auto starting emulator. """
    args = []

class EmulatorSettings(settings.Group):
    path: EmulatorExecutable = EmulatorExecutable()
    additional_args: EmulatorAdditionalArguments = EmulatorAdditionalArguments([ ])
    auto_start: bool = True

class ISOFile(settings.UserFilePath):
    """ Locate your Pokemon Colosseum ISO """
    description = "Pokemon Colosseum (USA) Iso"
    copy_to = None
    md5s = ["e3f389dc5662b9f941769e370195ec90"]

class PokemonColosseumSettings(settings.Group):
    iso_file: ISOFile = ISOFile(ISOFile.copy_to)
    dolphin_settings: EmulatorSettings = EmulatorSettings()
