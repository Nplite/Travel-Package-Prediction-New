from setuptools import find_packages, setup
from typing import List

requriment_file_name = "requirements.txt"
REMOVE_PACKAGE = "-e ."

def get_requirements()->List[str]:
    with open(requriment_file_name) as requirement_file:
        requriment_list = requirement_file.readline()
    requriment_list = [requriment_name.replace("\n", "") for requriment_name in requriment_list]

    if REMOVE_PACKAGE in requriment_list:
        requriment_list.remove(REMOVE_PACKAGE)
    return requriment_list



setup(name='Travel Package Prediction',
      version='0.0.1',
      description='Tourism Industry level project',
      author='Namdeo Patil',
      author_email='namdeopatil.1995@gmail.com',
      packages=find_packages(),
      install_reqires = get_requirements()
     )
