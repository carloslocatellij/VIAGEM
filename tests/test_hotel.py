import pytest
from modelos import hotel


nome = 'California'

h = modelos.hotel.Hotel(nome, 'San Francisco', 5, 6)


def test_hotel_nome():
    assert h.nome == 'Hotel California' , 'Ok'

test_hotel_nome()
