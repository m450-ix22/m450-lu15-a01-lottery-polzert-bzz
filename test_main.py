import pytest
from main import main
from authenticate import load_people

def test_main_exit(monkeypatch):
    people = load_people()
    person = people[0]
    inputs = iter(['geheim', 'Z'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    monkeypatch.setattr('authenticate.login', lambda: person)
    main()

def test_main_money(monkeypatch):
    people = load_people()
    person = people[0]
    inputs = iter(['geheim', 'A', 'E', '20', 'Z'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    monkeypatch.setattr('authenticate.login', lambda: person)
    main()
    assert person.balance == 34.00  # Assuming initial balance is 14.00 and 20.00 is deposited

def test_main_ticket(monkeypatch):
    people = load_people()
    person = people[0]
    inputs = iter(['geheim', 'B', '1', '2', '3', '4', '5', '6', '1', 'Z'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    monkeypatch.setattr('authenticate.login', lambda: person)
    main()
    assert person.balance == 12.00  # Assuming initial balance is 14.00 and ticket costs 2.00