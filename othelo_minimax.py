# -*- coding: utf8 -*-

import copy
import random
import time

EMPTY = '-'
BLACK = 'B'
WHITE = 'W'

DRAW = 'draw'


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

    def showBoard(self):
        for row in self.board:
            print '+'.join(row)
        print

    def getPossiblePositionList(self, nowColor):
        possiblePositionList = []

        for y in range(self.height):
            for x in range(self.width):
                if self.board[y][x] == EMPTY:
                    
                    isPossiblePosition = False
                    
                    for directionPair in self.directionPairList:
                        for direction in directionPair:
                            dy, dx = direction
                            nowY, nowX = y, x
                            flipCount = 0

                            while True:
                                nowY += dy
                                nowX += dx

                                if not self.isInBoard(nowY, nowX) or self.board[nowY][nowX] == EMPTY:
                                    flipCount = 0
                                    break
                                elif self.board[nowY][nowX] == nowColor:
                                    break
                                else:
                                    flipCount += 1

                            if flipCount != 0:
                                possiblePositionList.append((y, x))
                                isPossiblePosition = True
                                break

                        if isPossiblePosition:
                            break
    
        return possiblePositionList

    def setStone(self, color, position):
        if self.isValidPosition(color, position):
            y, x = position
            self.board[y][x] = color

            if color == WHITE:
                self.whiteCount += 1
            else:
                self.blackCount += 1
                
            self.flipStone(position)
            self.lastPosition = position
            self.lastColor = color

            return True
        
        return False

    def isValidPosition(self, color, position):
        return position in self.getPossiblePositionList(color)

    def flipStone(self, position):
        y, x = position
        nowColor = self.board[y][x]

        for directionPair in self.directionPairList:
            for direction in directionPair:
                dy, dx = direction
                nowY, nowX = y, x
                flipPositionList = []

                while True:
                    nowY += dy
                    nowX += dx

                    if not self.isInBoard(nowY, nowX) or self.board[nowY][nowX] == EMPTY:
                        flipPositionList = []
                        break
                    elif self.board[nowY][nowX] == nowColor:
                        break
                    else:
                        flipPositionList.append((nowY, nowX))

                for flipPosition in flipPositionList:
                    flipY, flipX = flipPosition
                    self.board[flipY][flipX] = nowColor

                flipCount = len(flipPositionList)
                
                if nowColor == WHITE:
                    self.whiteCount += flipCount
                    self.blackCount -= flipCount
                else:
                    self.whiteCount -= flipCount
                    self.blackCount += flipCount

    def isWin(self):
        if self.getPossiblePositionList(WHITE) == [] and self.getPossiblePositionList(BLACK) == []:
            if self.whiteCount > self.blackCount:
                return WHITE
            elif self.whiteCount < self.blackCount:
                return BLACK
            else:
                return DRAW
        else:
            return None

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

    state.showBoard()

    
    print "Success"


def minimax(state, depth, maxPlayer, firstCall=False):
    result = state.isWin()

    if result != None:
        if result == WHITE:
            return 100
        elif result == BLACK:
            return -100
        else:
            return 0
    elif depth == 0:
        return state.whiteCount - state.blackCount

    if maxPlayer:
        nowColor = WHITE
    else:
        nowColor = BLACK

    bestInfoList = []
    possiblePositionList = state.getPossiblePositionList(nowColor)

    for position in possiblePositionList:
        copyState = copy.deepcopy(state)
        copyState.setStone(nowColor, position)
        value = minimax(copyState, depth - 1, not maxPlayer)

        if bestInfoList == []:
            bestInfoList = [(value, position)]
        else:
            bestValue = bestInfoList[0][0]

            if value == bestValue:
                bestInfoList.append((value, position))
            elif (maxPlayer and value > bestValue) or (not maxPlayer and value < bestValue):
                bestInfoList = [(value, position)]

    if bestInfoList == []:
        bestInfoList = [(0, (0, 0))]

    if firstCall:
        return random.choice(bestInfoList)
    else:
        return bestInfoList[0][0]


def main():
    state = Board(8, 8)
    colorList = [WHITE, BLACK]
    turn = 0
    maxPlayer = True

    human = input()

    while True:

        nowColor = colorList[turn]

        state.showBoard()

        result = state.isWin()

        if result != None:
            break
        elif state.getPossiblePositionList(nowColor) == []:
            if state.lastColor == nowColor:
                break
            else:
                print nowColor
                print "No possible position"
        else:
            if turn == human:
                while True:
                    print "input:",
                    y, x = map(int, raw_input().split())
                    
                    if state.setStone(nowColor, (y, x)):
                        break

                    print nowColor
                    print "Wrong position"
            else:
                start = time.time()
                info = minimax(state, 4, maxPlayer, True)
                gap = time.time() - start

                state.setStone(nowColor, info[1])

                print nowColor
                print "Info:", info
                print "gap :", gap

        print

        turn = (turn + 1) % 2
        maxPlayer = not maxPlayer


    print "Win:", state.isWin()
    print "White:", state.whiteCount
    print "Black:", state.blackCount


if __name__ == "__main__":
    #test()
    main()
