import unittest
from hotel import Hotel


h = Hotel('Hotel California', 'San Francisco', 6)

def  test_hotel_nome():
    assert h.nome == 'Hotel California',  'Erro no nome'


if __name__ == '__main__':
    unittest.main()
