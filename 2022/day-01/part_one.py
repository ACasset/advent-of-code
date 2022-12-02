'''Day 01, part one'''

import sys
import os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
import functions

DAY = "01"
INPUT_TYPE = "real"

def main():
    '''Main function'''
    input_file = functions.read_file(DAY, INPUT_TYPE)

    current_sum = 0
    highest_sum = -1

    for line in input_file.split("\n"):
        if line:
            current_sum += int(line)
        else:
            highest_sum = max(highest_sum, current_sum)
            current_sum = 0

    print(highest_sum)

main()
