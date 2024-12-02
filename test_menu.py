import pytest
from menu import show_menu, select_menu

def test_show_menu(capsys):
    show_menu()
    captured = capsys.readouterr()
    assert 'Lotto' in captured.out

def test_select_menu(monkeypatch):
    inputs = iter(['A', 'B', 'Z'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    assert select_menu() == 'A'
    assert select_menu() == 'B'
    assert select_menu() == 'Z'