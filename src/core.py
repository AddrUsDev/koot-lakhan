# Standard library mports here:
from os import strerror
from pathlib import Path
from errno import ENOENT

# Third party imports:

# Local imports:
from config import settings
from errors import (
    InvalidArgumentException,
    InvalidFormatException,
    NoOperationSelected,
    TooManyArguments
)


class ArgumentParser:

    @staticmethod
    def __check_file_path__(file_path: str):
        file = Path(file_path)
        return file.is_file()
    
    @classmethod
    def parse_args(cls, argument_list: [str])-> {str, str}:
        modes, file_path_list = [], []
        i, arg_num = 0, len(argument_list)
        while i < arg_num:
            argument = argument_list[i]
            if argument.startswith('-'):
                if file_path_list and modes:
                    raise InvalidFormatException("""
                    File are given in invalid format, make sure all files
                    are given as space separated list at once.
                    """)
                
                elif argument in settings.ENCRYPT_ARGUMENTS:
                    modes.append("encrypt")

                elif argument in settings.DECRYPT_ARGUMENTS:
                    modes.append("decrypt")

                elif argument in settings.HELP_ARGUMENTS:
                    modes.append("help")
                
                else:
                    raise InvalidArgumentException("Invalid argument provided.")

            else:
                file_path_list.append(argument)
            
            i += 1

        if len(modes) > 1:
            raise TooManyArguments("selecting two many arguments at once.")

        elif len(modes) < 1:
            raise NoOperationSelected("""
            Please select a valid argument from provided options.
            Try: --help or -h for options.
            """)

        if not file_path_list and modes[0] != "help":
            raise FileNotFoundError(
                ENOENT, strerror(ENOENT), ""
                )

        for file_path in file_path_list:
            if not ArgumentParser.__check_file_path__(file_path):
                raise FileNotFoundError(
                    ENOENT, strerror(ENOENT), file_path
                    )

        return (modes[0], file_path_list)
