from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path:str) -> List[str]:
   
    requirement_list: List[str] = []
    try:
        with open(file_path, "r") as f:
            lines = f.readlines()
            for line in lines:
                requirement = line.strip()
                if requirement and requirement != "-e .":
                    requirement_list.append(requirement)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")

    return requirement_list

setup(
    name="my_MLOPS_leaning",
    version="0.1",
    author="Pasuwat",
    author_email="Pasuwat.sira@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)