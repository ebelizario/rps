'''App layer'''

import os
import sys

sys.path.insert(0, os.path.realpath(os.path.dirname(__file__)) + '/../lib')

from rps.constants import *
from rps.domain import Action


def play(move):
    action = Action(move)

    move = move.upper()
    cpu_move = action.cpu_move.upper()
    if action.outcome == STALEMATE:
        return '{} and {} is a stalemate!'.format(move, cpu_move)
    elif action.outcome == WIN:
        return '{} beats {}! You win!'.format(move, cpu_move)
    else:
        return '{} beats {}! You lose!'.format(cpu_move, move)
