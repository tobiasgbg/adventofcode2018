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

    def move(self, tracks):
        #print(str(self.direction))

        if self.direction == Direction.Left:
            self.x_pos = self.x_pos - 1
        elif self.direction == Direction.Right:
            self.x_pos = self.x_pos + 1
        elif self.direction == Direction.Up:
            self.y_pos = self.y_pos - 1
        elif self.direction == Direction.Down:
            self.y_pos = self.y_pos + 1

        #print(str(self.x_pos) + ' ' + str(self.y_pos))
        
        if tracks[self.x_pos][self.y_pos] == '+':
            if self.current_turn == 0:
                if self.direction == Direction.Left:
                    self.direction = Direction.Down
                elif self.direction == Direction.Right:
                    self.direction = Direction.Up
                elif self.direction == Direction.Up:
                    self.direction = Direction.Left
                elif self.direction == Direction.Down:
                    self.direction = Direction.Right
                self.current_turn += 1
            elif self.current_turn == 2:
                if self.direction == Direction.Left:
                    self.direction = Direction.Up
                elif self.direction == Direction.Right:
                    self.direction = Direction.Down
                elif self.direction == Direction.Up:
                    self.direction = Direction.Right
                elif self.direction == Direction.Down:
                    self.direction = Direction.Left
                self.current_turn = 0
            else:
                self.current_turn += 1
        elif tracks[self.x_pos][self.y_pos] == '\\':
            if self.direction == Direction.Right:
                self.direction = Direction.Down
            elif self.direction == Direction.Up:
                self.direction = Direction.Left
            elif self.direction == Direction.Left:
                    self.direction = Direction.Up
            elif self.direction == Direction.Down:
                self.direction = Direction.Right
        elif tracks[self.x_pos][self.y_pos] == '/':
            if self.direction == Direction.Right:
                self.direction = Direction.Up
            elif self.direction == Direction.Down:
                self.direction = Direction.Left
            elif self.direction == Direction.Left:
                self.direction = Direction.Down
            elif self.direction == Direction.Up:
                    self.direction = Direction.Right

def main():
    cwd = os.getcwd()
 
    with open (cwd + "/Day13Input.txt", "r") as myfile:
        file_list=myfile.readlines()

    trains = []
    tracks = [[0 for x in range(1000)] for y in range(1000)]
    x = 0
    y = 0
    for line in file_list:
        x = 0
        str_list = ''.join(line).replace('\n', '')
        list_char = list(str_list)

        for char in list_char:
            tracks[x][y] = char
            if (char == Direction.Left.value or char == Direction.Right.value or char is Direction.Up.value or char == Direction.Down.value):
                train = Train(Direction(char), len(trains) + 1, x, y)
                trains.append(train)
            x += 1
        y += 1

    #for train in trains:
        #print ('Train ' + str(train.name) + ' is at (' + str(train.x_pos) + ', ' + str(train.y_pos) + ')' + ' direction: ' + str(train.direction))

    TrainsHasCollided = False
    Collision_X = 0
    Collision_Y = 0
    while (not TrainsHasCollided):
        # sort trains based on position
        # starting from top and going downwards
        # left to right
        trains.sort(key=lambda x: x.x_pos)
        trains.sort(key=lambda y: y.y_pos)

        # move each train based on map
        for train in trains:
            train.move(tracks)
            #print ('Train ' + str(train.name) + ' is at (' + str(train.x_pos) + ', ' + str(train.y_pos) + ')')
            for other_train in trains:
                # check for collisions
                # if collision then stop
                if other_train.x_pos == train.x_pos and other_train.y_pos == train.y_pos and other_train.name != train.name:
                    print ('Oh no')
                    
                    TrainsHasCollided = True
                    Collision_X = train.x_pos
                    Collision_Y = train.y_pos

                    print(str(Collision_X) + ' ' + str(Collision_Y))

if __name__ == "__main__":
	main()