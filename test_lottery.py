
from lottery import create_ticket, select_numbers, print_ticket
from person import Person
from ticket import Ticket

def test_create_ticket(monkeypatch):
    person = Person('Test', 'password', 5.00)
    inputs = iter([1, 2, 3, 4, 5, 6, 1])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    create_ticket(person)
    assert person.balance == 3.00

def test_select_numbers(monkeypatch):
    ticket = Ticket(0, [])
    inputs = iter([1, 2, 3, 4, 5, 6, 1])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    select_numbers(ticket)
    assert len(ticket.numbers) == 6
    assert ticket.joker == 1