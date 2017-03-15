# -*- coding: utf8 -*-

from Board import *

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

    assert state.whiteCount == 4
    assert state.blackCount == 1
    assert state.getPossiblePositionList(BLACK) == [(2, 3), (2, 5), (4, 5)]

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

    assert state.whiteCount == 3
    assert state.blackCount == 3
    assert state.getPossiblePositionList(WHITE) == [(1, 2), (2, 2), (3, 2), (4, 2), (5, 2)]

    assert state.isWin() == None

    assert state.getBoardStr() == ("-" * 8    + "\n" +
                                   "-" * 8    + "\n" +
                                   "---BW---" + "\n" +
                                   "---BW---" + "\n" +
                                   "---BW---" + "\n" +
                                   "-" * 8    + "\n" +
                                   "-" * 8    + "\n" +
                                   "-" * 8)
                                  

    state.showBoard()

    
    print "Success"


if __name__ == "__main__":
    test()
