import pytest
from ticket import Ticket

def test_ticket_creation():
    ticket = Ticket(1, [1, 2, 3, 4, 5, 6])
    assert ticket.joker == 1
    assert ticket.numbers == [1, 2, 3, 4, 5, 6]

def test_ticket_invalid_joker():
    with pytest.raises(ValueError):
        Ticket('invalid', [1, 2, 3, 4, 5, 6])