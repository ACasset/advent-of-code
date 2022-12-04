'''Day 04, part two'''

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

main()
