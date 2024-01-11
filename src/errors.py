# Standard library imports:
import sys

# Third party imports

# Local imports

# Hiding traceback to show only error messages from our program.
sys.tracebacklimit = 0

# Error when unrecognised flag is passed in the program:
class InvalidArgumentException(BaseException):
    pass

# When multiple arguments are selected at once:
class TooManyArguments(BaseException):
    pass

# When no operation flag is selected:
class NoOperationSelected(BaseException):
    pass

# When file and flags are passed in wrong format:
class InvalidFormatException(BaseException):
    pass
