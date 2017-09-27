from setuptools import setup, find_packages
dependencies =[
]

VERSION = "0.1.0"

setup(
    name = 'folslib',
    packages = ['folslib'],
    version = VERSION,
    description = "Folger's Python Lib",
    author = 'Folger Lun',
    author_email = 'folger6@gmail.com',
    url = 'https://github.com/folger/folslib',
    download_url = 'https://github.com/folger/folslib/archive/{}.tar.gz'.format(VERSION), 
    keywords = ['hello', 'world'],
    include_package_data=True,
    requires=dependencies
)
