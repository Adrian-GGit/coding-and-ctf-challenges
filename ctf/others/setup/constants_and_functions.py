# terminal constants
QTERMINAL = "qterminal "
GNOME_TERMINAL = "gnome-terminal "
TERMINAL_TYPE = GNOME_TERMINAL
NEW_TAB = "--tab " if TERMINAL_TYPE == GNOME_TERMINAL else "unknown "

# setup constants
DIR = "dir"
TITLE = "title"
COMMAND = "command"

# setup specific constants
HACKING_DIR = "~/hacking/"
GOOGLE_CHROME = "google-chrome"
JUICESHOP_DOCKER = "sudo docker run --rm -p 3000:3000 bkimminich/juice-shop"

# platforms
OVERTHEWIRE = "overthewire"
HACKER101 = "hacker101"
JUICESHOP = "juiceshop"
TRYHACKME = "tryhackme"
PLATFORMS = [
    OVERTHEWIRE,
    HACKER101,
    JUICESHOP,
    TRYHACKME
]


def get_default_workspace(platform="", title="workspace"):
    return {
        TITLE: get_title(title),
        DIR: get_dir(HACKING_DIR + platform),
        COMMAND: "",
    }


def get_setup(title="setup", dir="~/", command=" "):
    return {
        TITLE: get_title(title),
        DIR: get_dir(dir),
        COMMAND: get_command(command),
    }


def get_title(title):
    terminals = {
        TERMINAL_TYPE == GNOME_TERMINAL: "--title=\"" + title + "\" "
    }
    return terminals[True]


def get_dir(dir):
    terminals = {
        TERMINAL_TYPE == GNOME_TERMINAL: "--working-directory " + dir + " "
    }
    return terminals[True]


def get_command(command):
    terminals = {
        TERMINAL_TYPE == GNOME_TERMINAL: "-- bash -c '" + command + "; exec bash' "
    }
    return terminals[True]
