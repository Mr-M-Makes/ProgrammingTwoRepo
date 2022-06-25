import sys
import subprocess
import pkg_resources
from pkg_resources import DistributionNotFound, VersionConflict
requirement_list = []
def should_install_requirement(requirement):
    should_install = False
    try:
        pkg_resources.require(requirement)
    except (DistributionNotFound, VersionConflict):
        should_install = True
    return should_install

def readFile(fileName):
        txt_file = open(fileName, "r")

        requirement_list = txt_file.read().splitlines()
        return requirement_list

def install_packages(requirement_list):
    try:
        requirements = [
            requirement
            for requirement in requirement_list
            if should_install_requirement(requirement)
        ]
        if len(requirements) > 0:
            subprocess.check_call([sys.executable, "-m", "pip", "install", *requirements])
        else:
            print("Requirements already satisfied.")

    except Exception as e:
        print(e)

requirement_list_dep = ['numpy', 'pandas', 'matplotlib', 'pillow', 'pendulum', 'moviepy', 'requests', 'pygame' ]
requirement_list = readFile("SetupNewComputer\Modules.txt")
print(requirement_list)
install_packages(requirement_list)
print(requirement_list)
print("Finished")