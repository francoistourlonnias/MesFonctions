"""
reservationClass.py module file
"""

def nextId(number):
    while True:
        number = number + 1
        yield number
    
num = nextId(99)

class Reservation():
    def __init__(self, reservationId, name,
                 flightData):
        self.reservationId = next(num)
        self.name = name
        self.flightData = flightData
