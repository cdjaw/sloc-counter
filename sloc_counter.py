#!/usr/bin/python3

import argparse
import re
import sys

__author__ = 'cdjaw'
__version__ = '0.1'


def parse_arguments():
    """Parse command line arguments and open input file as file object.

    :return: Parsed command line arguments
    :rtype: argparse.Namespace
    """
    parser = argparse.ArgumentParser(
        description='Count the Source Lines of Code (SLOC) without blank lines and comments.'
    )
    parser.add_argument(
        'source_file',
        help='absolute path to the source code file to be examined',
        type=argparse.FileType('r'),
    )
    parser.add_argument(
        '-v', '--version',
        action='version',
        version='%(prog)s version ' + __version__,
    )
    return parser.parse_args()


def filter_source_lines_of_code(file_contents: str = ''):
    """Return source lines of code after filtering comments and blank lines.

    :param str file_contents: Full source file contents to be filtered
    :return: Source lines of code
    :rtype: list[str]
    """
    source_lines_of_code = []
    file_contents = re.sub(r'/\*[\s\S]*?\*/', '', file_contents)                # filter block comments
    for line in file_contents.splitlines():
        line = re.sub(r'//.*$', '', line)                                       # filter line comments
        if len(line.strip()) > 0:                                               # filter blank lines
            source_lines_of_code.append(line)
    return source_lines_of_code


def main():
    arguments = parse_arguments()
    file_contents = arguments.source_file.read()
    source_lines_of_code = filter_source_lines_of_code(file_contents)
    print('SLOC:', len(source_lines_of_code))
    return 0


if __name__ == '__main__':
    sys.exit(main())
