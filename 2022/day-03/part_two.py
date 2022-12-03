'''Day 03, part two'''

import sys
import os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
import functions

DAY = "03"
INPUT_TYPE = "real"

def main():
    '''Main function'''
    input_file = functions.read_file(DAY, INPUT_TYPE)

    priorities = 0

    input_lines = input_file.split("\n")
    for i in range(0, len(input_lines), 3):
        first_line = input_lines[i]
        second_line = input_lines[i+1]
        third_line = input_lines[i+2]
                
        for char in first_line:
            try:
                second_line.index(char)
                char_index = third_line.index(char)
                priorities += get_priority_value(ord(third_line[char_index]))
                break
            except ValueError:
                pass

    print(priorities)

def get_priority_value(character_ord):
    if (character_ord >= 65 and character_ord <= 90):
        return character_ord - (64 - 26)
    
    if (character_ord >= 97 and character_ord <= 122):
        return character_ord - 96

main()
