from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    requirements = []
    with open(file_path, "r") as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

# perform setup parameters
setup(
    name="LLM_Project",
    version="0.0.1",
    author="Shayan Kumar",
    author_email="shayankumar765@gmail.com, shayankumar000@gmail.com",
    # install_requires=['pandas', 'numpy', 'sklearn'],
    install_requires=get_requirements("requirements.txt"),
    packages=find_packages()  # Add this line
)


# RUN:
# python setup.py bdist_wheel
# pip install /path_of_project/wheel_name
