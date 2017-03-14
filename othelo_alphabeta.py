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

    def getPoint(self, color):
        if color == WHITE:
            point = self.whiteCount
        else:
            point = self.blackCount

        cornerPositionList = [(0, 0), (0, self.width - 1), (self.height - 1, 0), (self.height - 1, self.width - 1)]

        for cornerPosition in cornerPositionList:
            cornerY, cornerX = cornerPosition

            if self.board[cornerY][cornerX] == color:
                point += 2

        for y in [0, self.height - 1]:
            for x in range(1, self.width - 1):
                if self.board[y][x] == color:
                    point += 1

        for y in range(1, self.height - 1):
            for x in [0, self.width - 1]:
                if self.board[y][x] == color:
                    point += 1

        return point

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


def alphabeta(state, depth, alpha, beta, maxPlayer, firstCall=False):
    result = state.isWin()

    if result != None:
        if result == WHITE:
            return 100
        elif result == BLACK:
            return -100
        else:
            return 0
    elif depth == 0:
        return state.getPoint(WHITE) - state.getPoint(BLACK)

    if maxPlayer:
        nowColor = WHITE
    else:
        nowColor = BLACK

    bestInfo = None
    possiblePositionList = state.getPossiblePositionList(nowColor)
    random.shuffle(possiblePositionList)

    for position in possiblePosition:
        copyState = copy.deepcopy(state)
        copyState.setStone(nowColor, position)
        value = alphabeta(copyState, depth - 1, alpha, beta, not maxPlayer)

        if maxPlayer and alpha < value:
            alpha = value
            bestInfo = (alpha, position)

            if beta <= alpha:
                break
        elif not maxPlayer and beta > value:
            beta = value
            bestInfo = (beta, position)


def main():
    print "main"


if __name__ == "__main__":
    main()
