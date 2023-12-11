from setuptools import find_packages, setup
from os import path, getcwd

__location__ = path.realpath(path.join(getcwd(), path.dirname(__file__)))


def read_requirements():
    """parses requirements from requirements.txt"""
    reqs_path = path.join(__location__, 'requirements.txt')
    with open(reqs_path, encoding='utf8') as fid:
        reqs = [
            line.strip() for line in fid if not line.strip().startswith('#')
        ]

    names = []
    links = []
    for req in reqs:
        if '://' in req:
            links.append(req)
        else:
            names.append(req)
    return {'install_requires': names, 'dependency_links': links}


setup(
    name="audio-app",
    version="0.1.0",
    packages=find_packages("requirements.txt"),
    tests_require=[
        "pytest",
    ],
    entry_points={
        "console_scripts": [
            "audio-app = audio_app.__main__:main"
        ]
    },
    author='pituganovstas@gmail.com',
    license='MIT',
    **read_requirements()

)
