class Bus:
    def __init__(self, number_seats, end, start, route_number):
        self.max_load = number_seats
        self.departure_town = start
        self.arrival = end
        self.route = route_number

    