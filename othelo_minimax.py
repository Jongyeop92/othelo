EMPTY = '-'
BLACK = 'B'
WHITE = 'W'


class Board:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = self.makeBoard(width, height)
        self.whiteCount = 2
        self.blackCount = 2
        self.lastPosition = None
        self.lastColor = None
        self.directionPairList = [[(-1, 0), ( 1,  0)],
                                  [(-1, 1), ( 1, -1)],
                                  [( 0, 1), ( 0, -1)],
                                  [( 1, 1), (-1, -1)]]

    def makeBoard(self, width, height):
        board = []

        for i in range(height):
            board.append([EMPTY] * width)

        board[3][3] = WHITE
        board[3][4] = BLACK
        board[4][3] = BLACK
        board[4][4] = WHITE

        return board
    
    def getBoard(self):
        return self.board

    def getPossiblePositionList(self, nowColor):
        return []

    def setStone(self, color, position):
        if self.isValidPosition(color, position):
            y, x = position
            self.board[y][x] = color
            self.flipStone(position)
            self.lastPosition = position
            self.lastColor = color

            return True
        
        return False

    def isValidPosition(self, color, position):
        return position in self.getPossiblePositionList(color)

    def flipStone(self, position):
        pass

    def isInBoard(self, y, x):
        return 0 <= y and y < self.height and 0 <= x and x < self.width


def test():

    state = Board(8, 8)

    assert state.getBoard() == [[EMPTY] * 8,
                                [EMPTY] * 8,
                                [EMPTY] * 8,
                                [EMPTY, EMPTY, EMPTY, WHITE, BLACK, EMPTY, EMPTY, EMPTY],
                                [EMPTY, EMPTY, EMPTY, BLACK, WHITE, EMPTY, EMPTY, EMPTY],
                                [EMPTY] * 8,
                                [EMPTY] * 8,
                                [EMPTY] * 8]

    assert state.whiteCount == 2
    assert state.blackCount == 2

    assert state.isInBoard(0, 0) == True
    assert state.isInBoard(4, 4) == True
    assert state.isInBoard(8, 8) == False
    assert state.isInBoard(-1, -1) == False

    assert state.getPossiblePositionList(WHITE) == [(2, 4), (3, 5), (4, 2), (5, 3)]
    assert state.getPossiblePositionList(BLACK) == [(2, 3), (3, 2), (4, 5), (5, 4)]

    assert state.isValidPosition(WHITE, (2, 4)) == True
    assert state.isValidPosition(WHITE, (0, 0)) == False
    assert state.isValidPosition(BLACK, (2, 3)) == True
    assert state.isValidPosition(BLACK, (1, 1)) == False

    assert state.setStone(WHITE, (1, 1)) == False
    assert state.setStone(WHITE, (2, 4)) == True
    assert state.getBoard() == [[EMPTY] * 8,
                                [EMPTY] * 8,
                                [EMPTY, EMPTY, EMPTY, EMPTY, WHITE, EMPTY, EMPTY, EMPTY],
                                [EMPTY, EMPTY, EMPTY, WHITE, WHITE, EMPTY, EMPTY, EMPTY],
                                [EMPTY, EMPTY, EMPTY, BLACK, WHITE, EMPTY, EMPTY, EMPTY],
                                [EMPTY] * 8,
                                [EMPTY] * 8,
                                [EMPTY] * 8]

    assert state.getPossiblePositionList(BLACK) == [(2, 3), (4, 5)]

    assert state.setStone(BLACK, (0, 0)) == False
    assert state.setStone(BLACK, (2, 3)) == True
    assert state.getBoard() == [[EMPTY] * 8,
                                [EMPTY] * 8,
                                [EMPTY, EMPTY, EMPTY, BLACK, WHITE, EMPTY, EMPTY, EMPTY],
                                [EMPTY, EMPTY, EMPTY, BLACK, WHITE, EMPTY, EMPTY, EMPTY],
                                [EMPTY, EMPTY, EMPTY, BLACK, WHITE, EMPTY, EMPTY, EMPTY],
                                [EMPTY] * 8,
                                [EMPTY] * 8,
                                [EMPTY] * 8]
    

    
    print "Success"


if __name__ == "__main__":
    test()
