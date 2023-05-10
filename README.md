# Maze

The purpose of this project is to solve the book Maze by Christopher Manson. 
The full title is Maze; Solve the World's Most Challenging Puzzle.

## Objective
The objective is to get from room 1 to room 45 and back to room 1 in as few steps as possible.
According to the author this is possible in 16 steps.

## Approach
The maze itself is laid out in `maze.json` where each key is a room, and each value is an array of doors in that room.
The project uses a breadth first search in order to find a route from 1 to 45.

ISBN 10: 0805010882
ISBN 13: 978-0805010886