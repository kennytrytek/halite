import random

from .constants import STILL, NORTH, EAST, SOUTH, WEST


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
        if direction == STILL:
            return x, y
        elif direction == NORTH:
            y = y - 1 if y else self.height - 1
        elif direction == EAST:
            x = (x + 1) % self.width
        elif direction == SOUTH:
            y = (y + 1) % self.height
        elif direction == WEST:
            x = x - 1 if x else self.width - 1

        return x, y

    def get_location(self, x, y, direction=STILL):
        x, y = self.translate_location(x, y, direction)
        return self.contents[y][x]

    def closest_non_owned_direction(self, x, y, my_id):
        starting_loc = self.get_location(x, y)
        left = nw = sw = right = ne = se = up = down = starting_loc
        distance = 0
        max_prod_loc = Location(x, y, production=0)
        max_prod_dir = None

        while True:
            distance += 1

            right = self.get_location(right.x, right.y, EAST)
            if right.owner != my_id and right.owner != 0:
                return EAST, right
            elif right.owner == 0 and right.production > max_prod_loc.production:
                max_prod_loc = right
                max_prod_dir = EAST

            down = self.get_location(down.x, down.y, SOUTH)
            if down.owner != my_id and down.owner != 0:
                return SOUTH, down
            elif down.owner == 0 and down.production > max_prod_loc.production:
                max_prod_loc = down
                max_prod_dir = SOUTH

            left = self.get_location(left.x, left.y, WEST)
            if left.owner != my_id and left.owner != 0:
                return WEST, left
            elif left.owner == 0 and left.production > max_prod_loc.production:
                max_prod_loc = left
                max_prod_dir = WEST

            up = self.get_location(up.x, up.y, NORTH)
            if up.owner != my_id and up.owner != 0:
                return NORTH, up
            elif up.owner == 0 and up.production > max_prod_loc.production:
                max_prod_loc = up
                max_prod_dir = NORTH

            if distance >= 3 and max_prod_loc.production > 0:
                return max_prod_dir, max_prod_loc

            if starting_loc.x == left.x:
                break

        direction = 10
        loc = self.get_location(x, y, direction)
        return direction, loc

    def closest_non_owned_direction_v9(self, x, y, my_id):
        starting_loc = self.get_location(x, y)
        left = right = up = down = starting_loc
        while True:  # Holds as long as map is square
            productions = []

            right = self.get_location(right.x, right.y, EAST)
            if right.owner != my_id and right.owner != 0:
                return EAST
            elif right.owner == 0:
                productions.append((right.production, EAST))

            down = self.get_location(down.x, down.y, SOUTH)
            if down.owner != my_id and down.owner != 0:
                return SOUTH
            elif down.owner == 0:
                productions.append((down.production, SOUTH))

            left = self.get_location(left.x, left.y, WEST)
            if left.owner != my_id and left.owner != 0:
                return WEST
            elif left.owner == 0:
                productions.append((left.production, WEST))

            up = self.get_location(up.x, up.y, NORTH)
            if up.owner != my_id and up.owner != 0:
                return NORTH
            elif up.owner == 0:
                productions.append((up.production, NORTH))

            if productions:
                return sorted(productions, reverse=True)[0][1]

            if starting_loc.x == left.x:
                break

        return random.choice([NORTH, EAST])
