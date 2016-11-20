import random

from . import context
from .common.constants import CARDINALS, DIRECTIONS, MAX_STRENGTH
from .common.hlt import Move


def move(loc):
    game_map = context.game_map
    my_id = context.my_id
    if loc.strength < loc.production or loc.strength < 20:
        return Move(loc, DIRECTIONS.STILL)

    weakest_neighbor = None
    weak_direction = None
    for d in CARDINALS.all():
        neighbor = game_map.get_location(loc.x, loc.y, d)
        if neighbor.owner != my_id and neighbor.strength < (loc.strength + 1):
            return Move(loc, d)
        elif neighbor.owner == my_id:
            if neighbor.strength > (loc.strength + 1) and (
                    neighbor.strength + loc.strength) < MAX_STRENGTH:
                return Move(loc, d)
            if (not weakest_neighbor or
                    neighbor.strength < weakest_neighbor.strength):
                weakest_neighbor = neighbor
                weak_direction = d

    if weakest_neighbor and weakest_neighbor.strength < 10:
        if loc.strength < 200:
            return Move(loc, DIRECTIONS.STILL)
        else:
            return Move(loc, random.choice([DIRECTIONS.SOUTH, DIRECTIONS.EAST]))

    return Move(loc, weak_direction or DIRECTIONS.STILL)
