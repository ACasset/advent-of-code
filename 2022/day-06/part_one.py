'''Day 06, part one'''

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

    for i in range(3, len(input_file)):
        elements = [input_file[i-3], input_file[i-2], input_file[i-1], input_file[i]]
        if len(set(elements)) == len(elements):
            print(i+1)
            return

main()
