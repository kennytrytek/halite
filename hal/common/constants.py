class DIRECTIONS:
    STILL = 0
    NORTH = 1
    EAST = 2
    SOUTH = 3
    WEST = 4

    @classmethod
    def all(cls):
        return [cls.STILL, cls.NORTH, cls.EAST, cls.SOUTH, cls.WEST]


class CARDINALS:
    NORTH = 1
    EAST = 2
    SOUTH = 3
    WEST = 4

    @classmethod
    def all(cls):
        return [cls.NORTH, cls.EAST, cls.SOUTH, cls.WEST]
