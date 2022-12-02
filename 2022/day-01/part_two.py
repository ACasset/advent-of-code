'''Day 01, part two'''

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
    sums = []

    for line in input_file.split("\n"):
        if line:
            current_sum += int(line)
        else:
            sums.insert(0, current_sum)
            current_sum = 0

    sums.sort(reverse = True)
    print(sums[0] + sums[1] + sums[2])

main()
