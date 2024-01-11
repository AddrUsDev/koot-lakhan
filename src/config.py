r"""
Defines the configurable settings for the encryption/decryption
"""

class Setting:
    # Flags accepted to run program in encrypt mode.
    ENCRYPT_ARGUMENTS= {
        "--encrypt",
        "-e",
    }
    # Flags accepted to run program in decrypt mode.
    DECRYPT_ARGUMENTS= {
        "--decrypt",
        "-d"
    }
    # Flags to print the help menu.
    HELP_ARGUMENTS= {
        "--help",
        "-h"
    }
    # Create a set of the allowed arguments that our program can accept.
    ALLOWED_ARGUMENTS= set()
    ALLOWED_ARGUMENTS= ALLOWED_ARGUMENTS.union(
        ENCRYPT_ARGUMENTS,
        DECRYPT_ARGUMENTS,
        HELP_ARGUMENTS
    )

# Initializing the settings object.
settings = Setting()
