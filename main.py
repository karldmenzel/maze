import json

from room import Room

#Load the maze JSON file
mazeFile = open('maze.json')
mazeData = json.load(mazeFile)

# Create the list of objects which will hold the rooms
rooms = []

# Convert JSON objects into Python objects
for num in range(45):
    newRoom = Room(num+1)
    doors = mazeData[str(num+1)]
    for door in doors:
        newRoom.doors.append(door)
    rooms.append(newRoom)

print("Rooms length " + str(len(rooms)))

# Print all the rooms and their doors
for roomInstance in rooms:
    print(roomInstance.tostring())
