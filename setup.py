from setuptools import setup, find_packages
import os
from typing import List

HYPHEN_DOT = "-e ."

def get_requirments(file) ->List[str]:
    """Read the requirements file and return the list of requirements
    args:
        file: str: file path
    return:
        List[str]: list of requirements
    """
    with open(file) as f:
        requirment =  f.read().splitlines()

    if HYPHEN_DOT in requirment:
        requirment.remove(HYPHEN_DOT)
    return requirment


setup(
    name='mahabharat_rag',
    version='0.1',
    packages=find_packages(),
    install_requires=get_requirments('requirements.txt')
)
    
    