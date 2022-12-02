'''Day 02, part one'''

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
        score += (ord(line.split(" ")[1]) - 87)
        # Outcome score
        score += define_outcome((ord(line.split(" ")[0]) - 64) - (ord(line.split(" ")[1]) - 87))

    print(score)

def define_outcome(shapes_difference):
    switch={
        -2: 0,
        -1: 6,
        0: 3,
        1: 0,
        2: 6,
    }
    return switch.get(int(shapes_difference))

main()
