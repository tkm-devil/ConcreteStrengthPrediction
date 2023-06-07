from setuptools import setup,find_packages
from typing import List

def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        return requirements

setup(
    name="Concrete_Strength_Prediction",
    version="1.0.0",
    description="A Production Grade Project",
    author="Tilak Kishor Mishra",
    author_email="tilakmishra949@gmail.com",
    install_requires=get_requirements('requirements.txt'),
    packages=find_packages()
)