'''Day 03, part one'''

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

    for line in input_file.split("\n"):
        # Split line
        first_compartment = line[:int(len(line) / 2)]
        second_compartment = line[int(len(line) / 2):]

        for char in first_compartment:
            try:
                char_index = second_compartment.index(char)
                priorities += get_priority_value(ord(second_compartment[char_index]))
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
