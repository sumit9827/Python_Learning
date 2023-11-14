""" Model for aircraft Flights. """

class Flight:

    def __init__(self, number, aircraft):
        if not number[:2].isalpha():
            raise ValueError (f"No Airline Code in '{number}'")
        if not number[2:].isdigit():
             raise ValueError (f"Invalid Airline Number in '{number}'")
        if not ( number[:2].isupper() and int(number[2:]) <=9999):
            raise ValueError (f"invalid route number '{number}'")
        self._number = number
        self._aircraft = aircraft

    def number(self):
        return self._number

    def airline(self):
        return self._number[:2]
    
    def aircraft_model(self):
        return self._aircraft_model()

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
        return (range(1, self._num_rows + 1), "ABCDEFGHJK"[:self._num_seats_per_row])
