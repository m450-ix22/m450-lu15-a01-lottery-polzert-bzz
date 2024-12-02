import pytest
from authenticate import login, load_people
from person import Person

def test_load_people():
    people = load_people()
    assert len(people) == 3
    assert isinstance(people[0], Person)

def test_login(monkeypatch):
    people = load_people()
    inputs = iter(['wrong', 'secrät', 'geheim'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    person = login()
    assert person.password == 'secrät'