from setuptools import find_packages, setup

NAME="ml-project-starter"
VERSION="0.0.1"
AUTHOR_NAME="Ahmad Nouh"
AUTHOR_EMAIL="ahmadnouh428@gmail.com"


HYPEN_E_DOT="-e ."

def get_requirements(file_path: str) -> list:
    """
    this function will return the list of requirements
    """
    requirements = []
    with open(file_path, "r") as f:
        requirements = [
            req.replace("\n", "") for req in f.readlines()
        ]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name=NAME,
    version=VERSION,
    author=AUTHOR_NAME,
    author_email=AUTHOR_EMAIL,
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)