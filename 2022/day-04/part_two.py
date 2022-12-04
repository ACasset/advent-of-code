'''Day 04, part two'''

import sys
import os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
import functions

DAY = "04"
INPUT_TYPE = "real"

def main():
    '''Main function'''
    input_file = functions.read_file(DAY, INPUT_TYPE)

    overlapping_assignments = 0

    for line in input_file.split("\n"):
        assignments = line.split(",")
        
        first_assignment = [*range(int(assignments[0].split('-')[0]), int(assignments[0].split('-')[1])+1)]
        second_assignment = [*range(int(assignments[1].split('-')[0]), int(assignments[1].split('-')[1])+1)]

        overlapping_assignments += check_if_in(first_assignment, second_assignment)

    print(overlapping_assignments)

def check_if_in(first_list, second_list):
    if (first_list[0] in second_list or first_list[len(first_list)-1] in second_list):
        return 1
    
    if (second_list[0] in first_list or second_list[len(second_list)-1] in first_list):
        return 1

    return 0

main()
