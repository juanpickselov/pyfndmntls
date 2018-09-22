import airtravel


def test_air_travel():
    the_result = airtravel.make_flights()
    print(str(the_result))
    assert the_result[0].__class__ == airtravel.Flight
    assert the_result[1].__class__ == airtravel.Flight
