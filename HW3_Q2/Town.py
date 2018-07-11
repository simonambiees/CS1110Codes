

class Town:
    def __init__(self, name, index, lead_to_first=None, lead_to_second=None):
        self.name = name
        self.first_road_to = lead_to_first
        self.second_road_to = lead_to_second
        self.people_here = None
        self.bus_here = None
        self.index = index
