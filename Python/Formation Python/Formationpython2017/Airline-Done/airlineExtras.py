class Aircraft:
    def __init__(self, aircraftCode=0, name=None):
        self.aircraftCode = aircraftCode
        self.name = name

class Airport:
    def __init__(self, citycode=None, city=None):
        self.citycode = citycode
        self.city = city