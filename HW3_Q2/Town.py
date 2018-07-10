class Town:
    def __init__(self, name, lead_to_first, lead_to_second):
        self.name = name
        self.first_road_to = lead_to_first.name
        self.second_road_to = lead_to_second.name