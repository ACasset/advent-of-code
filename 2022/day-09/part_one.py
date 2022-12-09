'''Day 09, part one'''

import sys
import os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
import functions
from typing import Set
import copy

DAY = "09"
INPUT_TYPE = "real"

def main():
    '''Main function'''
    input_file = functions.read_file(DAY, INPUT_TYPE)

    head = Position(0, 0)
    tail = Position(0, 0)
    visited_by_tail = set()
    visited_by_tail.add(tail)

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
                head.y += 1
            elif direction == "D":
                head.y -= 1
            elif direction == "L":
                head.x -= 1
            elif direction == "R":
                head.x += 1

            min_x = min(head.x, min_x)
            max_x = max(head.x, max_x)
            min_y = min(head.y, min_y)
            max_y = max(head.y, max_y)

            # Check if tail is pulled
            if abs(head.x - tail.x) <= 1 and abs(head.y - tail.y) <= 1:
            #if head.y-1 <= tail.y <= head.y+1 and head.x-1 <= tail.x <= head.x+1:
                continue

            # Pull tail
            if abs(head.x - tail.x) > 1:
                if head.y != tail.y:
                    if (head.y - tail.y) > 0:
                        tail.y += 1
                    else:
                        tail.y -= 1

                if (head.x - tail.x) > 0:
                    tail.x += 1
                else:
                    tail.x -= 1
            elif abs(head.y - tail.y) > 1:
                if head.x != tail.x:
                    if (head.x - tail.x) > 0:
                        tail.x += 1
                    else:
                        tail.x -= 1

                if (head.y - tail.y) > 0:
                    tail.y += 1
                else:
                    tail.y -= 1

            # Add new tail position to the set
            visited_by_tail.add(copy.deepcopy(tail))

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

main()
