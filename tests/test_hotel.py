import modelos.hotel as hotel


h = hotel.Hotel('Hotel California', 'San Francisco', 6)

def  test_hotel_nome():
    assert h.nome == 'Hotel California',  'Erro no nome'

