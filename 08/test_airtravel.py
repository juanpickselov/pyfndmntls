from airtravel import *


flyte = Flight('AA0600')
print(type(flyte))
print(flyte.flight_num())
print(flyte.airline())

another_flyte = Flight('NW200')
print(another_flyte.airline())
print(another_flyte.flight_num())

flyte_bad_num = Flight('US9000')
flyte_bad_num_too = Flight('US1234')

a_flight = Aircraft('G-EUPT', 'Airbus A319', num_rows=22, num_seats_per_row=6)
print(a_flight.registration())
print(a_flight.model())
print(a_flight.seating_plan())

