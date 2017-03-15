# -*- coding: utf8 -*-

from Board import *

import copy
import random

def minimax(state, depth, maxPlayer, firstCall=False):
    result = state.isWin()

    if result != None:
        if result == WHITE:
            return INFINITE
        elif result == BLACK:
            return -INFINITE
        else:
            return 0
    elif depth == 0:
        return state.getPoint(WHITE) - state.getPoint(BLACK)

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
        return 0

    if firstCall:
        return random.choice(bestInfoList)
    else:
        return bestInfoList[0][0]


def alphabeta(state, depth, alpha, beta, maxPlayer, firstCall=False):
    result = state.isWin()

    if result != None:
        if result == WHITE:
            return INFINITE
        elif result == BLACK:
            return -INFINITE
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

    for position in possiblePositionList:
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

            if beta <= alpha:
                break

    if bestInfo == None:
        if maxPlayer:
            value = INFINITE
        else:
            value = -INFINITE

        if firstCall:
            return (value, possiblePositionList[0])
        else:
            return value

    if firstCall:
        return bestInfo
    else:
        return bestInfo[0]
