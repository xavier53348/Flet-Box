from pathlib import Path
from setuptools import setup , find_packages
import os
# import pypandoc
import sys

# NECESARY TO CREATE PACKAGES
# pip install pathlib
# pip install pypandoc
# pip install twine
# pip install wheel

# sudo apt-get install python3-dev
# sudo apt-get install python3-pip

#: MAKE A SETUP INSTALL
# python3 setup.py sdist bdist_wheel
# python3 setup.py bdist_wheel
# python3 setup.py register -r pypi
# python3 setup.py sdist upload -r pypi

# python setup.py sdist
# twine upload dist/* -r pypi
# twine upload dist/* -r flet_box_gui

# python setup.py sdist bdist_wheel --universal
# twine upload dist/* -r pypi

# pip install twine ,pypandoc
# twine upload dist/*
# twine check dist/*
# PACKAGE META-DATA

# python3 -m pip install --upgrade pip
# pip install pypandoc
# pip install pypandoc_binary

# errors pip
# sudo apt install libgpgme-dev swig
# pip install --upgrade gpg

NAME            = 'flet-box-gui'
DESCRIPTION     = "flet-box-gui it's a GUI Dragg and drop BUILDER."
PLATAFORM       = 'Multy platforms'
REQUIRES_PYTHON = '>=3.8'

AUTHOR          = 'xavier53348'
EMAIL           = 'xavier53348@gmail.com'
MANTAINER       = 'xavier53348'
MANTAINER_EMAIL = 'xavier53348@gmail.com'

URL           = 'https://github.com/xavier53348/Flet-Box'
ROADMAP       = 'https://github.com/xavier53348/Flet-Box/blob/main/docs/Roadmap.md'
CREATE_WIDGET = 'https://github.com/xavier53348/Flet-Box/blob/main/docs/WIDGET.md'
CHANGE_LOG    = 'https://github.com/xavier53348/Flet-Box/blob/main/docs/CHANGELOG.md'

REQUIRED       = [
'flet','flet-core','flet-runtime','g4f','pyperclip'
]
PAKAGES_IMAGES = {
'assets':['*'],
}
RUN_IN_CONSOLE ={
"console_scripts": [
"flet_box      = flet_box:run_app",
],
}

PYPY_KEYWORDS_TO_FIND = ["flet-box-gui", "flet",'flet-gui','flet-builder','flet-sdk']

# read the contents of your README file
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()



# try:
#     long_description = pypandoc.convert_file('README.md', 'rst')
# except(IOError, ImportError):
#     long_description = open('README.md').read()
#     data = "\n\tpip install pypandoc\n\tpip install pypandoc_binary"
#     print(f'Please install {data}')

#: MANAGE VERSION
here = os.path.abspath(os.path.dirname(__file__))

try:
    with open(os.path.join(here, 'VERSION'), encoding='utf-8') as f:
        VERSION = f.read()

except FileNotFoundError:
    VERSION = '0.1.0'

PROJECT_DOCUMENTATION = {
    "Documentation": CREATE_WIDGET,
    "GitHub": URL,
    "Changelog": CHANGE_LOG ,
    "Roadmap":ROADMAP,

}

setup(
    #: PERSONAL DATA
    name                          = NAME,
    author                        = AUTHOR,
    author_email                  = EMAIL,
    maintainer                    = MANTAINER,
    maintainer_email              = MANTAINER_EMAIL,

    #: PROJECT DESCRIOPTION
    description                   =  DESCRIPTION,
    long_description              = long_description,
    long_description_content_type = 'text/markdown',
    url                           = URL,
    project_urls                  = PROJECT_DOCUMENTATION,

    #: DISTRIBUTION
    platforms            = PLATAFORM,
    version              = VERSION,
    packages             = find_packages(),

    #: EXTRA FILES INCLUID
    include_package_data = True,
    package_data         = PAKAGES_IMAGES,

    #: INSTALL DEPENDENCIES
    install_requires     = REQUIRED,

    # RUN APP BY TERMINAL WITH THE TAG NAME
    entry_points         = RUN_IN_CONSOLE,

    #: KEYWORDS TO PYPY
    keywords             = PYPY_KEYWORDS_TO_FIND,

    classifiers          = [
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        # Development Status :: 1 - Planning
        # Development Status :: 2 - Pre-Alpha
        # Development Status :: 3 - Alpha
        # Development Status :: 4 - Beta
        # Development Status :: 5 - Production/Stable
        # Development Status :: 6 - Mature
        # Development Status :: 7 - Inactive

        'Development Status :: 1 - Planning',
        "Topic :: Software Development :: Build Tools",
        'Intended Audience :: Developers',
        'Natural Language :: English',
        # 'License :: OSI Approved :: Apache License',

        "License :: OSI Approved :: MIT License",
        # "License :: OSI Approved :: GNU General Public License (GPL)"
        # "License :: OSI Approved :: GNU General Public License v2 (GPLv2)"
        # "License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)"
        # "License :: OSI Approved :: GNU General Public License v3 (GPLv3)"
        # "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)"
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',

        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
    )


