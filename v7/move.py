import random

from . import context
from .common.constants import CARDINALS, DIRECTIONS, MAX_STRENGTH
from .common.hlt import Move


def move(loc):
    game_map = context.game_map
    my_id = context.my_id
    if loc.strength < loc.production and loc.strength < 20:
        return Move(loc, DIRECTIONS.STILL)

    weakest_neighbor_strength = 15
    for d in CARDINALS.all():
        neighbor = game_map.get_location(loc.x, loc.y, d)
        if neighbor.owner != my_id:
            weakest_neighbor_strength = min(
                weakest_neighbor_strength, neighbor.strength)

            if neighbor.strength < (loc.strength - 1):
                return Move(loc, d)

        # elif neighbor.owner == my_id:
        #     if neighbor.strength >= loc.strength and (
        #             neighbor.strength + loc.strength) < MAX_STRENGTH:
        #         return Move(loc, d)

    # Nobody around to merge with, and I'm pathetic
    if loc.strength < 60:
        return Move(loc, DIRECTIONS.STILL)

    quadrant = game_map.closest_non_owned_quadrant(loc.x, loc.y, my_id)
    if quadrant == 1:
        return Move(loc, random.choice([DIRECTIONS.NORTH, DIRECTIONS.WEST]))
    elif quadrant == 2:
        return Move(loc, random.choice([DIRECTIONS.NORTH, DIRECTIONS.EAST]))
    elif quadrant == 3:
        return Move(loc, random.choice([DIRECTIONS.SOUTH, DIRECTIONS.WEST]))
    else:
        return Move(loc, random.choice([DIRECTIONS.SOUTH, DIRECTIONS.EAST]))
