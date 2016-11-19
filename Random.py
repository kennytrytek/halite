import random
from hal.common.hlt import *
from hal.common.networking import *

my_id, game_map = getInit()
sendInit("Random")

while True:
    moves = []
    game_map = getFrame()
    for y in range(game_map.height):
        for x in range(game_map.width):
            loc = game_map.get_location(x, y)
            if loc.owner == my_id:
                moves.append(Move(loc, random.choice(DIRECTIONS.all())))

    sendFrame(moves)
