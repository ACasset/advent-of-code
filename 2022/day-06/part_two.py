'''Day 06, part two'''

import sys
import os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
import functions

DAY = "06"
INPUT_TYPE = "real"

def main():
    '''Main function'''
    input_file = functions.read_file(DAY, INPUT_TYPE)

    for i in range(13, len(input_file)):
        elements = []

        for j in range(i-13, i+1):
            elements += input_file[j]

        if len(set(elements)) == len(elements):
            print(i+1)
            return

main()
