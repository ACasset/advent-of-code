'''Day 09, part two'''

import sys
import os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
import functions
from typing import List
import copy

DAY = "09"
INPUT_TYPE = "test"

def main():
    '''Main function'''
    input_file = functions.read_file(DAY, INPUT_TYPE)

    rope_length: int = 10

    # Build rope
    rope: List[Position] = List[Position]
    for i in range(rope_length):
        rope.append(Position(0, 0))

    # Build visited list
    visited_by_tail = set()
    visited_by_tail.add(copy.deepcopy(rope[rope_length-1]))

    min_x = 0
    max_x = 0
    min_y = 0
    max_y = 0

    for line in input_file.split("\n"):
        direction = line.split(" ")[0]
        steps = line.split(" ")[1]

        for i in range(int(steps)):
            # Move head
            if direction == "U":
                rope[0].y += 1
            elif direction == "D":
                rope[0].y -= 1
            elif direction == "L":
                rope[0].x -= 1
            elif direction == "R":
                rope[0].x += 1

            min_x = min(rope[0].x, min_x)
            max_x = max(rope[0].x, max_x)
            min_y = min(rope[0].y, min_y)
            max_y = max(rope[0].y, max_y)

            # Check if tail is pulled
            if abs(rope[0].x - rope[rope_length-1].x) <= 1 and abs(rope[0].y - rope[rope_length-1].y) <= 1:
            #if head.y-1 <= tail.y <= head.y+1 and head.x-1 <= tail.x <= head.x+1:
                continue

            # Pull tail
            if abs(rope[0].x - rope[rope_length-1].x) > 1:
                if rope[0].y != rope[rope_length-1].y:
                    if (rope[0].y - rope[rope_length-1].y) > 0:
                        rope[rope_length-1].y += 1
                    else:
                        rope[rope_length-1].y -= 1

                if (rope[0].x - rope[rope_length-1].x) > 0:
                    rope[rope_length-1].x += 1
                else:
                    rope[rope_length-1].x -= 1
            elif abs(rope[0].y - rope[rope_length-1].y) > 1:
                if rope[0].x != rope[rope_length-1].x:
                    if (rope[0].x - rope[rope_length-1].x) > 0:
                        rope[rope_length-1].x += 1
                    else:
                        rope[rope_length-1].x -= 1

                if (rope[0].y - rope[rope_length-1].y) > 0:
                    rope[rope_length-1].y += 1
                else:
                    rope[rope_length-1].y -= 1

            # Add new tail position to the set
            visited_by_tail.add(copy.deepcopy(rope[rope_length-1]))

    print(len(visited_by_tail))

class Position:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented

        return self.x == other.x and self.y == other.y

def display_positions(min_x, max_x, min_y, max_y, rope):
    for y in reversed(range(min_y, max_y+1)):
        for x in range(min_x, max_x+1):
            current_position = Position(x, y)

            rope_displayed = False
            for i in range(len(rope)):
                if rope[i] == current_position:
                    print(str(i), end="")
                    rope_displayed = True

            if not rope_displayed:
                print(".", end="")
        print("")

main()
