import pytest
import template


def test_template(capsys):
    captured = capsys.readouterr()
    assert captured.out =="Hello World!\n"
