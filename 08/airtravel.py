'''Model for flights'''


class Flight:

    def __init__(self, flight_number):
        if not flight_number[:2].isalpha():
            raise ValueError("No ariline code in '{}'".format(flight_number))

        if not flight_number[:2].isupper():
            raise ValueError("Invalid airline code '{}'".format(flight_number))

        if not (flight_number[2:].isdigit() and int(flight_number[2:]) <= 9999):
            raise ValueError("Invalid route number '{}'".formmat(flight_number))

        self._flight_number = flight_number

    def flight_num(self):
        return self._flight_number

    def airline(self):
        return self._flight_number[:2]

class Aircraft:

    def __init__(self, registration, model, num_rows, num_seats_per_row):
        self._registration = registration
        self._model = model
        self._num_rows = num_rows
        self._num_seats_per_row = num_seats_per_row

    def registration(self):
        return self._registration

    def model(self):
        return self._model

    def seating_plan(self):
        return (range(1, self._num_rows + 1),
                'ABCDEFGHJK'[:self._num_seats_per_row])
