import os
import argparse
import importlib
from constants_and_functions import COMMAND, DIR, NEW_TAB, TERMINAL_TYPE, TITLE, PLATFORMS

# TODO: open chrome and but so that terminal tab can be used for commands
# => https://superuser.com/questions/513496/how-can-i-run-a-command-from-the-terminal-without-blocking-it

parser = argparse.ArgumentParser(description='Apply setup for specific hacking platform.')
exclusive_parser = parser.add_mutually_exclusive_group()
for platform in PLATFORMS:
    command = "--" + platform
    exclusive_parser.add_argument(
        command,
        action="store_true",
        help=platform
    )

args = parser.parse_args()
called_module = None
for arg in args._get_kwargs():
    if arg[1]:
        called_module = arg[0]
        break

if called_module:
    module = importlib.import_module(f"{called_module}.{called_module}_constants")
    tabs_dir = getattr(module, "TABS_DIR")

    for tab_dirs in tabs_dir:
        os.system(TERMINAL_TYPE + NEW_TAB + tab_dirs[TITLE] + tab_dirs[DIR] + tab_dirs[COMMAND])
else:
    parser.print_help()
