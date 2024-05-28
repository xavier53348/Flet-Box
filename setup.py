from setuptools import setup , find_packages
import os

#: MAKE A SETUP INSTALL
# python3 setup.py sdist bdist_wheel
# python3 setup.py bdist_wheel

# pip install twine
# twine upload dist/*
# PACKAGE META-DATA

NAME            = 'flet_box'
DESCRIPTION     = "Flet-Box it's a GUI Dragg dropp BUILDER."
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

PYPY_KEYWORDS_TO_FIND = ["flet-Box", "flet", "fletbox",'flet-gui','flet-builder','flet-sdk']

here = os.path.abspath(os.path.dirname(__file__))

#: MANAGE README
try:
    with open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
        long_description = '\n' + f.read()

except FileNotFoundError:
    long_description = DESCRIPTION

#: MANAGE VERSION
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
    name                 = NAME,
    author               = AUTHOR,
    author_email         = EMAIL,
    maintainer           = MANTAINER,
    maintainer_email     = MANTAINER_EMAIL,

    #: PROJECT DESCRIOPTION
    description          = DESCRIPTION,
    long_description     = long_description,
    url                  = URL,
    project_urls         = PROJECT_DOCUMENTATION,

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

        # "License :: OSI Approved :: GNU General Public License (GPL)"
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        # "License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)"
        # "License :: OSI Approved :: GNU General Public License v3 (GPLv3)"
        # "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)"

        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
    )


