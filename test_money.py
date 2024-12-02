import pytest
from money import transfer_money, select_transaction
from person import Person

def test_transfer_money(monkeypatch):
    person = Person('Test', 'password', 10.00)
    inputs = iter(['E', 20.00, 'Z'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    transfer_money(person)
    assert person.balance == 30.00

def test_select_transaction(monkeypatch):
    inputs = iter(['A', 'E', 'Z'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    assert select_transaction() == 'A'
    assert select_transaction() == 'E'
    assert select_transaction() == 'Z'