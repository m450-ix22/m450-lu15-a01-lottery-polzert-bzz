import pytest
from person import Person

def test_person_creation():
    person = Person('Test', 'password', 10.00)
    assert person.givenname == 'Test'
    assert person.password == 'password'
    assert person.balance == 10.00

def test_person_invalid_balance():
    with pytest.raises(ValueError):
        Person('Test', 'password', 'invalid')