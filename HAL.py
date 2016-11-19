import random

from hal.common.constants import DIRECTIONS
from hal.common.hlt import Location, Move
from hal.common.networking import getFrame, getInit, sendFrame, sendInit

my_id, game_map = getInit()
sendInit("HAL")

while True:
    moves = []
    game_map = getFrame()
    for y in range(game_map.height):
        for x in range(game_map.width):
            location = Location(x, y)
            if game_map.getSite(location).owner == my_id:
                moves.append(Move(location, random.choice(DIRECTIONS)))
    sendFrame(moves)
