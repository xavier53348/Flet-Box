#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Note: To use the 'upload' functionality of this file, you must:
# >>> $ pipenv install twine --dev
# >>> make wheel
# >>> python3 setup.py sdist bdist_wheel

# --name              print package name
# --version (-V)      print package version
# --fullname          print <package name>-<version>
# --author            print the author's name
# --author-email      print the author's email address
# --maintainer        print the maintainer's name
# --maintainer-email  print the maintainer's email address
# --contact           print the maintainer's name if known, else the author's
# --contact-email     print the maintainer's email address if known, else the
#                     author's
# --url               print the URL for this package
# --license           print the license of the package
# --licence           alias for --license
# --description       print the package description
# --long-description  print the long package description
# --platforms         print the list of platforms
# --classifiers       print the list of classifiers
# --keywords          print the list of keywords
# --provides          print the list of packages/modules provided
# --requires          print the list of packages/modules required
# --obsoletes         print the list of packages/modules made obsolete

import io
import os
import sys
from shutil import rmtree
from distutils.core import setup
from setuptools import find_packages,  Command

# Package meta-data.
NAME            = 'flet-box'
DESCRIPTION     = "Flet-Box it's a GUI Dragg dropp BUILDER."
URL             = 'https://github.com/xavier53348/Flet-Box'
AUTHOR          = 'xavier53348'
EMAIL           = 'xavier53348@gmail.com'
MANTAINER       = 'xavier53348'
MANTAINER_EMAIL = 'xavier53348@gmail.com'
REQUIRES_PYTHON = '>=3.8'
PLATAFORM       = 'Multy platforms'
VERSION         = '0.0.2'
DATA_FILES      = [ 'src']
# What packages are required for this module to be executed?
REQUIRED = [
    # 'requests', 'maya', 'records',
    'flet','flet-core','flet-runtime'
]

# What packages are optional?
EXTRAS = {
    # 'fancy feature': ['django'],
}

# The rest you shouldn't have to touch too much :)
# ------------------------------------------------
# Except, perhaps the License and Trove Classifiers!
# If you do change the License, remember to change the Trove Classifier for that!

here = os.path.abspath(os.path.dirname(__file__))

# Import the README and use it as the long-description.
# Note: this will only work if 'README.md' is present in your MANIFEST.in file!
try:
    with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
        long_description = '\n' + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION

# Load the package's __version__.py module as a dictionary.
about = {}
if not VERSION:
    project_slug = NAME.lower().replace("-", "_").replace(" ", "_")
    with open(os.path.join(here, project_slug, '__version__.py')) as f:
        exec(f.read(), about)
else:
    about['__version__'] = VERSION


class UploadCommand(Command):
    """Support setup.py upload."""

    description = 'Build and publish the package.'
    user_options = []

    @staticmethod
    def status(s):
        """Prints things in bold."""
        print('\033[1m{0}\033[0m'.format(s))

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            self.status('Removing previous builds…')
            rmtree(os.path.join(here, 'dist'))
        except OSError:
            pass

        self.status('Building Source and Wheel (universal) distribution…')
        os.system('{0} setup.py sdist bdist_wheel --universal'.format(sys.executable))

        self.status('Uploading the package to PyPI via Twine…')
        os.system('twine upload dist/*')

        self.status('Pushing git tags…')
        os.system('git tag v{0}'.format(about['__version__']))
        os.system('git push --tags')

        sys.exit()


# Where the magic happens:
setup(
    name                             = NAME,
    version                          = about['__version__'],
    description                      = DESCRIPTION,
    long_description                 = long_description,
    long_description_content_type    = 'WIDGET.md',
    author                           = AUTHOR,
    author_email                     = EMAIL,
    python_requires                  = REQUIRES_PYTHON,
    maintainer                       = MANTAINER,
    maintainer_email                 = MANTAINER_EMAIL,
    url                              = URL,
    # If your package is a single module, use this instead of 'packages':
    # py_modules                     =['mypackage'],

    # entry_points                   ={
    #     'console_scripts': ['mycli =mymodule:cli'],
    # },
    platforms                        = PLATAFORM,
    install_requires                 = REQUIRED,
    extras_require                   = EXTRAS,
    data_files                       = DATA_FILES,
    include_package_data             = True,
    # packages                         = ['src'],
    # data_files                       = [('share/doc/foo', ['happy_birthday-art.txt'])],
    packages                         = find_packages(),
     # packages                        = ["flet_box",],
    # package_data                     ={'flet_box': ['flet_box/*'],},
    # exclude_package_data             = {'src': ['src'],},
    license                          = 'apache-2.0',
    keywords                         = ["flet-Box", "flet",'flet-gui','flet-builder','flet-sdk'],
    requires                         = ["flet"],
    obsoletes                        = [],
    classifiers                      = [
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 5 - Production/Untable',
        "Topic :: Software Development :: Build Tools",
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: apache-2.0',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
    # $ setup.py publish support.
    cmdclass                         = {
        'upload': UploadCommand,
    },
)


