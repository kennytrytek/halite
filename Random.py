import random

from hal.common.constants import DIRECTIONS
from hal.common.hlt import Location, Move
from hal.common.networking import getFrame, getInit, sendFrame, sendInit

myID, gameMap = getInit()
sendInit("RandomBot")

while True:
    moves = []
    gameMap = getFrame()
    for y in range(gameMap.height):
        for x in range(gameMap.width):
            location = Location(x, y)
            if gameMap.getSite(location).owner == myID:
                moves.append(Move(location, random.choice(DIRECTIONS)))
    sendFrame(moves)
