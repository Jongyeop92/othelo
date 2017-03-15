from __future__ import division

from random import choice
from math import log, sqrt
import datetime
import copy

class MonteCarlo(object):

    def __init__(self, **kwargs):
        seconds = kwargs.get('time', 30)
        self.calculation_time = datetime.timedelta(seconds=seconds)

        self.max_moves = kwargs.get('max_moves', 10)

        self.wins = {}
        self.plays = {}

    def update(self, state):
        pass

    def get_play(self, state, player):
        self.max_depth = 0
        legal = state.getPossiblePositionList(player)

        if not legal:
            return
        elif len(legal) == 1:
            return legal[0]

        games = 0
        begin = datetime.datetime.utcnow()
        while datetime.datetime.utcnow() - begin < self.calculation_time:
            self.run_simulation()
            games += 1

        moves_states = []
        for p in legal:
            copy_state = copy.deepcopy(state)
            copy_state.setStone(player, p)
            moves_states.append((p, copy_state))

        print games, datetime.datetime.utcnow() - begin

        percent_wins, move = max(
            (self.wins.get((player, S.getBoardStr()), 0) /
             self.plays.get((player, S.getBoardStr()), 1),
             p)
            for p, S in moves_states
        )

        for x in sorted(
            ((100 * self.wins.get((player, S.getBoardStr()), 0) /
              self.plays.get((player, S.getBoardStr()), 1),
              self.wins.get((player, S.getBoardStr()), 0),
              self.plays.get((player, S.getBoardStr()), 0), p)
             for p, S in moves_states),
            reverse=True
        ):
            print "{3}: {0: .2f}% ({1} / {2})".format(*x)

        print "Maximum depth searched:", self.max_depth

    def run_simulation(self, state, player):
        plays, wins = self.plays, self.wins
        
        visited_states = set()

        expand = True
        for t in xrange(1, self.max_moves + 1):
            legal = state.getPossiblePositionList(player)
            
            moves_states = []
            for p in legal:
                copy_state = copy.deepcopy(state)
                copy_state.setStone(player, p)
                moves_states.append((p, copy_state))

            if all(plays.get((player, S.getBoardStr())) for p, S in moves_states):
                log_total = log(
                    sum(plays[(player, S.getBoardStr())] for p, S in moves_states))
                value, move, state = max(
                    ((wins[(player, S.getBoardStr())] / plays[(player, S.getBoardStr())]) +
                     self.C * sqrt(log_total / plays[(player, S.getBoardStr())]), p, S)
                    for p, S in moves_states
                )
            else:
                move, state = choice(moves_states)

            if expand and (player, state) not in plays:
                expand = False
                plays[(player, state.getBoardStr())] = 0
                wins[(player, state.getBoardStr())] = 0
                if t > self.max_depth:
                    self.max_depth = t

            visited_states.add((player, state))

            player = self.board.current_player(state)
            winner = state.isWin()
            if winner:
                break

        for player, state in visited_states:
            if (player, state.getBoardStr()) not in self.plays:
                continue
            self.plays[(player, state.getBoardStr())] += 1
            if player == winner:
                self.wins[(player, state.getBoardStr())] += 1


