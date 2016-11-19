from . import context
from .common.constants import CARDINALS, DIRECTIONS
from .common.hlt import Move


def move(loc):
    game_map = context.game_map
    my_id = context.my_id
    if loc.strength < loc.production:
        return Move(loc, DIRECTIONS.STILL)

    for d in CARDINALS.all():
        neighbor = game_map.get_location(loc.x, loc.y, d)
        if neighbor.owner != my_id and neighbor.strength < (loc.strength + 1):
            return Move(loc, d)
        elif neighbor.owner == my_id and neighbor.strength > (loc.strength + 1):
            return Move(loc, d)

    return Move(loc, DIRECTIONS.STILL)
