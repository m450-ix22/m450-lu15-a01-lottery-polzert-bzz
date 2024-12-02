import pytest
from numeric_input import read_int, read_float

def test_read_int(monkeypatch):
    inputs = iter([5, 50])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    assert read_int('Prompt', 1, 10) == 5
    assert read_int('Prompt', 1, 100) == 50

def test_read_float(monkeypatch):
    inputs = iter([5.5, 50.5])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    assert read_float('Prompt', 1.0, 10.0) == 5.5
    assert read_float('Prompt', 1.0, 100.0) == 50.5