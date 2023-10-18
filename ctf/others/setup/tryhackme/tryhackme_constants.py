from constants_and_functions import GOOGLE_CHROME, TRYHACKME, get_default_workspace, get_setup

TRYHACKME_WORKSPACE = get_default_workspace(platform=TRYHACKME)
TRYHACKME_CHROME = get_setup(title=GOOGLE_CHROME, command=GOOGLE_CHROME)

TABS_DIR = [
    TRYHACKME_WORKSPACE,
    TRYHACKME_CHROME,
]
