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

print("Loaded " + str(len(rooms)) + " rooms")

# Print all the rooms and their doors
# for roomInstance in rooms:
#     print(roomInstance.tostring())

checkedRooms = []

def checkRoom(currentRoom, path, destination):
    # Uncomment this to see each path, helpful for optimization
    # print("Checking " + path)
    
    if(currentRoom.roomNumber in checkedRooms):
        return
    else:
        checkedRooms.append(currentRoom.roomNumber)
    
    if(currentRoom.roomNumber == destination):
        print("Found route: " + path)
    else:
        for door in currentRoom.doors:
            checkRoom(rooms[door-1], path + ", " + str(door), destination)

checkRoom(rooms[0], "1", 45)

# Need to reset checkedRooms after each run
checkedRooms = []

checkRoom(rooms[44], "45", 1)

