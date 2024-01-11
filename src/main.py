# Standard library imports:
from sys import argv

# Third party imports

# Local imports
from core import ArgumentParser

if __name__ == "__main__":
    mode, file_path = ArgumentParser.parse_args(argv[1:])
    print(mode, file_path)
