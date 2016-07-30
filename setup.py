"magnificent"
from setuptools import find_packages, setup
from magnificent import __version__

def read_file(path):
    result = []
    try:
        with open(path) as f:
            result = f.readlines()
    except Exception as err:
        pass
    return result

install_requires = read_file('requirements.txt')
tests_require = read_file('test-requirements.txt')

name = 'magnificent'

setup(
    name=name,
    version=__version__,
    description='magnificent',
    packages=find_packages(),
    install_requires=install_requires,
    tests_require=tests_require,
    entry_points={
        "console_scripts":[
            'magnificent_start=magnificent.app:run',
            'magnificent_healthcheck=magnificenthealthcheck.app:run',
        ]
    },
)
