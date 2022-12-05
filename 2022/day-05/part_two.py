'''Day 05, part two'''

import sys
import os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
import functions

DAY = "05"
INPUT_TYPE = "real"

def main():
    '''Main function'''
    input_file = functions.read_file(DAY, INPUT_TYPE)
    input_lines = input_file.split("\n")

    stacks_numbers_line = find_stacks_numbers_line(input_lines)
    stacks_number = find_stacks_number(input_lines, stacks_numbers_line)
    stacks = fill_stacks(input_lines, stacks_number, stacks_numbers_line)
    stacks = move_stacks(input_lines, stacks_numbers_line, stacks)
    print(get_top_elements(stacks))

def find_stacks_numbers_line(input_lines):
    for i in range(0, len(input_lines)-1):
        if input_lines[i][1].isdigit():
            return i

def find_stacks_number(input_lines, stacks_numbers_line):
    return int(input_lines[stacks_numbers_line][len(input_lines[stacks_numbers_line])-2])

def fill_stacks(input_lines, stacks_number, stacks_numbers_line):
    stacks = [ [0] * 0 for i in range(0, stacks_number) ]

    for i in range(0, stacks_number):
        for j in reversed(range(0, stacks_numbers_line)):
            stack_index = 1 + (4 * i)
            if input_lines[j][stack_index] != ' ':
                stacks[i] += input_lines[j][stack_index]

    return stacks

def move_stacks(input_lines, stacks_numbers_line, stacks):
    for i in range(stacks_numbers_line+2, len(input_lines)):
        instructions = input_lines[i].split(' ')
        moved_elements = stacks[int(instructions[3])-1][-int(instructions[1]):]
        print(moved_elements)
        del stacks[int(instructions[3])-1][-int(instructions[1]):]
        for k in range(len(moved_elements)):
            stacks[int(instructions[5])-1].append(moved_elements[k])

    return stacks

def get_top_elements(stacks):
    top_elements = ""
    for i in range(len(stacks)):
        top_elements += stacks[i][-1]
    return top_elements

main()
