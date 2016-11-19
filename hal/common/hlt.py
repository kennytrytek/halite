import copy
import math

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

    def in_bounds(self, l):
        is_within_x = 0 <= l.x < self.width
        is_within_y = 0 <= l.y < self.height
        return is_within_x and is_within_y

    def getDistance(self, l1, l2):
        dx = abs(l1.x - l2.x)
        dy = abs(l1.y - l2.y)
        if dx > self.width / 2:
            dx = self.width - dx
        if dy > self.height / 2:
            dy = self.height - dy
        return dx + dy

    def getAngle(self, l1, l2):
        dx = l2.x - l1.x
        dy = l2.y - l1.y

        if dx > self.width - dx:
            dx -= self.width
        elif -dx > self.width + dx:
            dx += self.width

        if dy > self.height - dy:
            dy -= self.height
        elif -dy > self.height + dy:
            dy += self.height
        return math.atan2(dy, dx)

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
