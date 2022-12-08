'''Day 08, part one'''

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
    print(count_visible_trees(tree_map))

def create_map(input_file) -> List[List[int]]:
    input_lines = input_file.split("\n")
    output_map = []
    for input_line in input_lines:
        current_line = []
        for input_column in range(len(input_line)):
            current_line.append(int(input_line[input_column]))

        output_map.append(current_line)

    return output_map

def count_visible_trees(tree_map: List[List[int]]):
    if len(tree_map) != len(tree_map[0]):
        exit(-1)

    visible_trees: int = 0

    # North and south side
    visible_trees += len(tree_map)
    visible_trees += len(tree_map)

    # East and west side
    visible_trees += len(tree_map) - 2
    visible_trees += len(tree_map) - 2

    # Heart of the forest
    for x in range(1, len(tree_map)-1):
        for y in range(1, len(tree_map)-1):
            if is_tree_visible(tree_map, x, y):
                visible_trees += 1

    return visible_trees

def is_tree_visible(tree_map, x_coord, y_coord) -> bool:
    tree_height = tree_map[y_coord][x_coord]

    visible = True

    # Visible from the west side ?
    for x in range(x_coord):
        if tree_map[y_coord][x] >= tree_height:
            visible = False
            break

    if visible:
        return True

    visible = True

    # Visible from the north side ?
    for y in range(y_coord):
        if tree_map[y][x_coord] >= tree_height:
            visible = False
            break

    if visible:
        return True

    visible = True

    # Visible from the east side ?
    for x in range(x_coord+1, len(tree_map)):
        if tree_map[y_coord][x] >= tree_height:
            visible = False
            break

    if visible:
        return True

    visible = True

    # Visible from the south side ?
    for y in range(y_coord+1, len(tree_map)):
        if tree_map[y][x_coord] >= tree_height:
            visible = False
            break

    if visible:
        return True

    return False

main()
