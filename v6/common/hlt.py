import random

from .constants import DIRECTIONS


class Location(object):
    def __init__(self, x=0, y=0, owner=0, strength=0, production=0):
        self.x = x
        self.y = y
        self.owner = owner
        self.strength = strength
        self.production = production


class Move(object):
    def __init__(self, loc, direction):
        self.loc = loc
        self.direction = direction

    def __str__(self):
        return '{x} {y} {dir} '.format(
            x=self.loc.x, y=self.loc.y, dir=self.direction)


class GameMap(object):
    def __init__(self, width=0, height=0, numberOfPlayers=0):
        self.width = width
        self.height = height
        self.contents = []

        for y in range(0, self.height):
            row = []
            for x in range(0, self.width):
                row.append(Location(x, y, 0, 0, 0))
            self.contents.append(row)

    def translate_location(self, x, y, direction):
        if direction == DIRECTIONS.STILL:
            return x, y
        elif direction == DIRECTIONS.NORTH:
            y = y - 1 if y else self.height - 1
        elif direction == DIRECTIONS.EAST:
            x = (x + 1) % self.width
        elif direction == DIRECTIONS.SOUTH:
            y = (y + 1) % self.height
        elif direction == DIRECTIONS.WEST:
            x = x - 1 if x else self.width - 1

        return x, y

    def get_location(self, x, y, direction=DIRECTIONS.STILL):
        x, y = self.translate_location(x, y, direction)
        return self.contents[y][x]

    def closest_non_owned_quadrant(self, x, y, my_id):
        row = self.contents[y]
        column = [self.contents[a][x] for a in range(0, self.height)]
        right_of_x = row[x:]
        left_of_x = row[:x]
        left_of_x.reverse()
        if len(right_of_x) < len(left_of_x):
            while len(right_of_x) < len(left_of_x):
                right_of_x.append(left_of_x.pop())

        elif len(left_of_x) < len(right_of_x):
            while len(left_of_x) < len(right_of_x):
                left_of_x.append(right_of_x.pop())

        above_y = column[:y]
        above_y.reverse()
        below_y = column[y:]
        if len(below_y) < len(above_y):
            while len(below_y) < len(above_y):
                below_y.append(above_y.pop())

        elif len(above_y) < len(below_y):
            while len(above_y) < len(below_y):
                above_y.append(below_y.pop())

        while left_of_x or right_of_x or above_y or below_y:
            if left_of_x and left_of_x[0].owner == my_id:
                left_of_x.pop(0)
            else:
                return 1

            if above_y and above_y[0].owner == my_id:
                above_y.pop(0)
            else:
                return 2

            if right_of_x and right_of_x[0].owner == my_id:
                right_of_x.pop(0)
            else:
                return 4

            if below_y and below_y[0].owner == my_id:
                below_y.pop(0)
            else:
                return 3

        return random.choice(range(1, 5))

