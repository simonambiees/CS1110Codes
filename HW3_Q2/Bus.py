
class Bus:
    def __init__(self, number_seats, start, end, route_number, status="atStart"):
        self.max_load = number_seats
        self.departure_town = end
        self.arrival_town = start
        self.route = route_number
        self.people_on = []
        self.status = status
