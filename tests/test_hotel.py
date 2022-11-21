import unittest

from hotel import Hotel


h = Hotel('Hotel California', 'San Francisco', 6)


class main(unittest.TestCase):

    def test_hotel_nome(self):
        assert h.nome == 'Hotel California',  'Erro no nome'


if __name__ == '__main__':
    unittest.main()
