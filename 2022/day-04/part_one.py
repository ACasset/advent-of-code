'''Day 04, part one'''

import sys
import os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
import functions

DAY = "04"
INPUT_TYPE = "test"

def main():
    '''Main function'''
    input_file = functions.read_file(DAY, INPUT_TYPE)

    overlapping_assignments = 0

    for line in input_file.split("\n"):
        assignments = line.split(",")
        first_assignment = range(assignments[0].split('-')[0], assignments[0].split('-')[1])
        second_assignment = range(assignments[1].split('-')[0], assignments[1].split('-')[1])
        print(first_assignment)
        print(second_assignment)

    print(overlapping_assignments)

main()