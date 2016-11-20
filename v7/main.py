from .common.networking import getFrame, sendFrame, sendInit
from .move import move
from . import context

sendInit("HAL")


def main():
    my_id = context.my_id
    while True:
        moves = []
        context.game_map = getFrame(my_id)
        game_map = context.game_map
        for y in range(game_map.height):
            for x in range(game_map.width):
                loc = game_map.get_location(x, y)
                if loc.owner == my_id:
                    moves.append(move(loc))

        sendFrame(moves)
        context.round_num += 1
