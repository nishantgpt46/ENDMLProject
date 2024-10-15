from setuptools import find_packages, setup
from typing import List

# This is used to identify local installs or editable installs
hyphen_e_dot = '-e .'

# Function to extract requirements from a file and return a list of them
def get_requirements(file_path: str) -> List[str]:
    '''
    This function reads the requirements.txt file and returns a list of requirements.
    It removes any editable installs (i.e., '-e .') from the list.
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        # Strip newline characters
        requirements = [req.replace("\n", "") for req in requirements]
        
        # Remove '-e .' from the list if present
        if hyphen_e_dot in requirements:
            requirements.remove(hyphen_e_dot)
    
    return requirements


# Metadata and dependencies for the package setup
setup(
    name='MLE2EPROJECT',  # Correct project name
    version='0.0.1',
    author='Nishant',
    author_email='nishantgpt46@gmail.com',
    packages=find_packages(),
    # Dynamically get install requirements from the requirements.txt file
    install_requires=get_requirements('requirements.txt')
)
