import random

from . import context
from .common.constants import STILL, NORTH, EAST, SOUTH, WEST, MAX_STRENGTH
from .common.hlt import Move


def move(loc):
    # if context.round_num < 75:
    return v10_move(loc)

    # return v9_move(loc)


def v10_move(loc):
    game_map = context.game_map
    my_id = context.my_id

    direction, destination = game_map.closest_non_owned_direction(
        loc.x, loc.y, my_id)

    next_loc = game_map.get_location(loc.x, loc.y, direction)

    # if destination.production >= (loc.production + 2):
    if next_loc.owner != my_id:
        if next_loc.strength <= loc.strength:
            return Move(loc, direction)

        if next_loc.strength <= (loc.strength + loc.production * 2):
            return Move(loc, STILL)
    else:
        if ((loc.strength + next_loc.strength + next_loc.production) >= destination.strength) and next_loc.strength > 20:
            return Move(loc, direction)
        elif loc.strength < 50:
            for d in [WEST, NORTH, EAST, SOUTH]:
                neighbor = game_map.get_location(loc.x, loc.y, d)
                if neighbor.owner != my_id:
                    if loc.strength >= neighbor.strength:
                        return Move(loc, d)

            return Move(loc, STILL)

    for d in [WEST, NORTH, EAST, SOUTH]:
        neighbor = game_map.get_location(loc.x, loc.y, d)
        if neighbor.owner != my_id:
            if loc.strength >= neighbor.strength:
                return Move(loc, d)

    if loc.strength > 50:
        return Move(loc, direction)

    return Move(loc, STILL)


def v9_move(loc):
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

    direction = game_map.closest_non_owned_direction_v9(loc.x, loc.y, my_id)
    return Move(loc, direction)
