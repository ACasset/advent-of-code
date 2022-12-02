'''Day 02, part two'''

import sys
import os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
import functions

DAY = "02"
INPUT_TYPE = "real"

def main():
    '''Main function'''
    input_file = functions.read_file(DAY, INPUT_TYPE)

    score = 0

    for line in input_file.split("\n"):
        # Shape score
        score += define_shape(line.split(" ")[0], line.split(" ")[1])
        # Outcome score
        score += define_outcome(line.split(" ")[1])

    print(score)

def define_shape(opponent_shape, expected_outcome):
    switch={
        'AX': 3,
        'AY': 1,
        'AZ': 2,
        'BX': 1,
        'BY': 2,
        'BZ': 3,
        'CX': 2,
        'CY': 3,
        'CZ': 1,
    }
    return switch.get(opponent_shape + expected_outcome)

def define_outcome(expected_outcome):
    switch={
        'X': 0,
        'Y': 3,
        'Z': 6,
    }
    return switch.get(expected_outcome)

main()
