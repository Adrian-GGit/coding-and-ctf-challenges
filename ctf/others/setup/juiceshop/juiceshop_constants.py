from constants_and_functions import JUICESHOP, JUICESHOP_DOCKER, get_default_workspace, get_setup

JUICESHOP_WORKSPACE = get_default_workspace(platform=JUICESHOP)
JUICESHOP_DOCKER = get_setup(title="juiceshop-docker", command=JUICESHOP_DOCKER)

TABS_DIR = [
    JUICESHOP_WORKSPACE,
    JUICESHOP_DOCKER,
]
