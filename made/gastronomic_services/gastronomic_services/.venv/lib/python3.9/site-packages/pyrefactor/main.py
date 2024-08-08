#!/usr/bin/env python
import argparse
import logging
import sys

parser = argparse.ArgumentParser(usage="%(prog)s [options] args...")
parser.add_argument("-f", "--inputfile", type=argparse.FileType("r"), default="-")
subparsers = parser.add_subparsers(help="Action to be taken")

def _action(name):
    def decorator(func):
        parser = subparsers.add_parser(name)
        parser.set_defaults(action=func)
        return parser
    return decorator

def make_processor(function_name):
    module_name, function_name = function_name.rsplit(".", 1)
    module = __import__(module_name, fromlist=[''])
    func = getattr(module, function_name)
    @_action(function_name.split(".")[-1])
    def cmd(args):
        _process(args, func)
        return 0

make_processor("pyrefactor.dict_styles.toggle_dict_style")
make_processor("pyrefactor.assertions.toggle_assert_style")

def _process(args, func):
    sys.stdout.write(func(args.inputfile.read()))

#### For use with entry_points/console_scripts
def main_entry_point():
    args = parser.parse_args()
    sys.exit(args.action(args))


if __name__ == "__main__":
    main_entry_point()
