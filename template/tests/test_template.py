import pytest
from template import hello_world


def test_template(capsys):
    hello_world()
    captured = capsys.readouterr()
    assert captured.out =="Hello, World!\n"
