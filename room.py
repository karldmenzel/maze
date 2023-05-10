class Room:

    def __init__(self, roomNumber):
        self.roomNumber = roomNumber
        self.doors = []

    def tostring(self):
        return f'Room {self.roomNumber}: {self.doors}'