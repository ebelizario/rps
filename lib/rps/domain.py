'''Domain layer'''

import random
from rps.constants import *


class Action(object):
    def __init__(self, player_move):
        self.player_move = player_move
        self.cpu_move = self.cpu_move()
    
    def cpu_move(self):
        return random.choice(POSSIBLE_MOVES.keys())

    @property
    def outcome(self):
        if self.player_move == self.cpu_move:
            return STALEMATE
        elif self.player_move in POSSIBLE_MOVES[self.cpu_move]:
            return WIN
        return LOSE 
