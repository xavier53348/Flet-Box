#!/bin/bash

# keyring set https://upload.pypi.org/legacy/ __token__
# pypi-AgEIcHlwaS5vcmcCJDhkOWM0Nzg3LTc2YjktNDUxYi1iZjRkLWE1YzA2YzI5MmJmZgACFFsxLFsiZmxldC1ib3gtZ3VpIl1dAAIsWzIsWyI2OTA5MDc0NC0yMTFlLTQwMjQtOTgzZC0xYWFlYTFkN2M2MDYiXV0AAAYghC_YrIbHvn2RvWV6CoWWyjxpTKEE9ZLmMRu74p4ZuGY

rm -r dist/*
rm -dr flet_box_gui.egg-info

./bump-version.sh

python3 setup.py sdist bdist_wheel
twine check dist/*
# twine upload dist/*