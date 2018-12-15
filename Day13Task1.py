import os
import sys
import re
from enum import Enum

class Direction(Enum):
    Up = '^'
    Down = 'v'
    Left = '<'
    Right = '>'
    No = 0

class Train:
    def __init__(self, direction, name, x_pos, y_pos):
        self.direction = Direction(direction)
        self.name = name
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.current_turn = 0

    name = 0
    x_pos = 0
    y_pos = 0
    direction = Direction.No
    current_turn = 0

    def move(self, map):
        self.x_pos = self.x_pos
        self.y_pos = self.y_pos

def main():
    cwd = os.getcwd()
 
    with open (cwd + "/Day13Input.txt", "r") as myfile:
        file_list=myfile.readlines()

    trains = []
    x = 0
    y = 0
    for line in file_list:
        x = 0
        str_list = ''.join(line).replace('\n', '')
        list_char = list(str_list)

        for char in list_char:
            print char
            if (char == Direction.Left.value or char == Direction.Right.value or char is Direction.Up.value or char == Direction.Down.value):
                train = Train(Direction(char), len(trains) + 1, x, y)
                trains.append(train)
            x += 1
        y += 1

    for train in trains:
        print ('Train ' + str(train.name) + ' is at (' + str(train.x_pos) + ', ' + str(train.y_pos) + ')')

    # sort trains based on position
    # starting from top and going downwards
    # left to right

    # move each train based on map

    # check for collisions
    # if collision then stop

    # sort trains again

    # und so weiter

if __name__ == "__main__":
	main()