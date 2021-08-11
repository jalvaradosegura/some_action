import os
import pathlib

from some_action.tmp_file import TempFile


def test_create_and_delete_tmp_folder():
    with TempFile('tmp_', 'my_file', 'some content'):
        assert pathlib.Path('tmp_').exists()
    assert not pathlib.Path('tmp_').exists()


def test_create_file_inside_the_tmp_folder():
    with TempFile('tmp_', 'my_file', 'some content'):
        assert pathlib.Path('tmp_/my_file').exists()
        assert len(os.listdir('tmp_')) == 1


def test_file_content():
    with TempFile('tmp_', 'my_file', 'some content') as tmp_file:
        assert tmp_file.read() == 'some content'
