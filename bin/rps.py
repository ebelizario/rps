'''
This is a rock paper scissor game
'''

import argparse
import os
import sys

sys.path.insert(0, os.path.realpath(os.path.dirname(__file__)) + '/../lib')

import rps.application as app_layer


def play(move):
    print app_layer.play(move)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='rock paper scissor')
    parser.add_argument('move', choices=app_layer.get_moves(),
                        help='your move')
    args = parser.parse_args()
    play(args.move)
