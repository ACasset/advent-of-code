'''Day 08, part two'''

import sys
import os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
import functions
from typing import List

DAY = "08"
INPUT_TYPE = "real"

def main():
    '''Main function'''
    input_file = functions.read_file(DAY, INPUT_TYPE)

    tree_map = create_map(input_file)

    max_tree_score: int = 0
    for x in range(1, len(tree_map)-1):
        for y in range(1, len(tree_map)-1):
            max_tree_score = max(get_tree_score(tree_map, x, y), max_tree_score)

    print(max_tree_score)

def create_map(input_file) -> List[List[int]]:
    input_lines = input_file.split("\n")
    output_map = []
    for input_line in input_lines:
        current_line = []
        for input_column in range(len(input_line)):
            current_line.append(int(input_line[input_column]))

        output_map.append(current_line)

    return output_map

def get_tree_score(tree_map, x_coord, y_coord) -> int:
    tree_height = tree_map[y_coord][x_coord]

    # West side
    west_score: int = 0
    for x in reversed(range(x_coord)):
        west_score += 1
        if tree_map[y_coord][x] >= tree_height:
            break

    # North side
    north_score: int = 0
    for y in reversed(range(y_coord)):
        north_score += 1
        if tree_map[y][x_coord] >= tree_height:
            break

    # East side
    east_score: int = 0
    for x in range(x_coord+1, len(tree_map)):
        east_score += 1
        if tree_map[y_coord][x] >= tree_height:
            break

    # South side
    south_score: int = 0
    for y in range(y_coord+1, len(tree_map)):
        south_score += 1
        if tree_map[y][x_coord] >= tree_height:
            break

    return north_score * south_score * east_score * west_score

main()
