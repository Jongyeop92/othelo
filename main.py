# -*- coding: utf8 -*-

from Board import *
from GameAI import *
from MonteCarlo import *

import time

def main():
    
    state = Board(8, 8)
    colorList = [WHITE, BLACK]
    turn = 0
    maxPlayer = True

    monteCarlo = MonteCarlo(time=10, max_moves=100)

    minTime = None
    maxTime = None
    totalTime = 0
    count = 0

    human = input()

    while True:

        nowColor = colorList[turn]

        print "White:", state.whiteCount
        print "Black:", state.blackCount
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

                if nowColor == WHITE:
                    info = monteCarlo.get_play(state, nowColor)
                    #info = minimax(state, 3, maxPlayer, True)
                    #info = alphabeta(state, 5, -INFINITE, INFINITE, maxPlayer, True)
                    pass
                else:
                    #info = monteCarlo.get_play(state, nowColor)
                    info = minimax(state, 3, maxPlayer, True)
                    pass
                
                #info = minimax(state, 3, maxPlayer, True)
                #info = alphabeta(state, 3, -INFINITE, INFINITE, maxPlayer, True)
                #info = monteCarlo.get_play(state, nowColor)
                
                gap = time.time() - start

                if minTime == None or gap < minTime:
                    minTime = gap

                if maxTime == None or gap > maxTime:
                    maxTime = gap

                totalTime += gap
                count += 1

                state.setStone(nowColor, info[1])

                print nowColor
                print "Info:", info
                print "Gap :", gap

        print

        turn = (turn + 1) % 2
        maxPlayer = not maxPlayer


    print "Win:", state.isWin()
    print "White:", state.whiteCount
    print "Black:", state.blackCount
    print
    print "MinTime  :", minTime
    print "MaxTime  :", maxTime
    print "MeanTime :", (totalTime / count)
    print "TotalTime:", totalTime
    print
    print "Count:", count


if __name__ == "__main__":
    main()
