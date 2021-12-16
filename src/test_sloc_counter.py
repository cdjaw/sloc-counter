#!/usr/bin/python3

import os
import pytest

import sloc_counter

__author__ = 'cdjaw'
__version__ = '0.2'


@pytest.fixture
def test_files_base_path():
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), 'test_files')


# (abbreviations: LC = Line Comment, BC = Block Comment, WS = White Spaces)
@pytest.mark.parametrize('source_code_file, sloc_count', [
    ('CommentsOnly.cpp', 0),
    ('Empty.txt', 0),
    ('HelloWorld.cpp', 6),
    ('HelloWorld_BC.cpp', 6),
    ('HelloWorld_BC_inline.cpp', 6),
    ('HelloWorld_BC_inline_multiline.cpp', 6),
    ('HelloWorld_LC.cpp', 6),
    ('HelloWorld_LC__inline.cpp', 6),
    ('HelloWorld_LC_BC.cpp', 6),
    ('HelloWorld_LC_BC_WS_mixed.cpp', 6),
    ('HelloWorld_LC_BC_nested.cpp', 6),
    ('HelloWorld_WS.cpp', 6),
])
def test_filter_source_lines_of_code(
        test_files_base_path,
        source_code_file,
        sloc_count
):
    absolute_source_file_path = os.path.join(test_files_base_path, source_code_file)
    with open(absolute_source_file_path) as input_file:
        source_lines_of_code = sloc_counter.filter_source_lines_of_code(input_file.read())
        assert len(source_lines_of_code) == sloc_count
