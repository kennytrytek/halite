import random

from . import context
from .common.constants import STILL, NORTH, EAST, SOUTH, WEST, MAX_STRENGTH
from .common.hlt import Move


def move(loc):
    game_map = context.game_map
    my_id = context.my_id
    if loc.strength < loc.production and loc.strength < 20:
        return Move(loc, STILL)

    weakest_neighbor_strength = 999
    for d in [WEST, NORTH, EAST, SOUTH]:
        neighbor = game_map.get_location(loc.x, loc.y, d)
        if neighbor.owner != my_id:
            weakest_neighbor_strength = min(
                weakest_neighbor_strength, neighbor.strength)

            if neighbor.strength < (loc.strength - 1):
                return Move(loc, d)

    if loc.strength < 60:
        return Move(loc, STILL)

    direction = game_map.closest_non_owned_direction(loc.x, loc.y, my_id)
    return Move(loc, direction)
    # if quadrant == 1:
    #     return Move(loc, random.choice([NORTH, WEST]))
    # elif quadrant == 2:
    #     return Move(loc, random.choice([NORTH, EAST]))
    # elif quadrant == 3:
    #     return Move(loc, random.choice([SOUTH, WEST]))
    # else:
    #     return Move(loc, random.choice([SOUTH, EAST]))
