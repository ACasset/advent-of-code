'''Day 07, part one'''

import sys
import os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
import functions
from typing import List

DAY = "07"
INPUT_TYPE = "real"

def main():
    '''Main function'''
    input_file = functions.read_file(DAY, INPUT_TYPE)

    tree = create_tree(input_file)
    print(browse_tree(tree))

class FileSystemItem:
    def __init__(self, name: str, parent: "FileSystemItem"):
        self.name = name
        self.parent = parent
        self.size = 0

    def get_name(self):
        return self.name

    def get_parent(self):
        return self.parent

    def get_size(self):
        return int(self.size)

class Folder(FileSystemItem):
    def __init__(self, name, parent):
        super().__init__(name, parent)
        self.children = []

    def add_child(self, child: FileSystemItem):
        self.children.append(child)

    def get_children(self) -> List[FileSystemItem]:
        return self.children

    def get_size(self):
        total_size = 0

        for child in self.children:
            total_size += child.get_size()

        return total_size

class File(FileSystemItem):
    def __init__(self, name: str, parent: FileSystemItem, size: int):
        super().__init__(name, parent)
        self.size = size

def create_tree(input_file) -> Folder:
    root_folder = Folder("/", None)
    current_folder = root_folder
    for line in input_file.split("\n"):
        if line.split(" ")[0] == "$":
            if line.split(" ")[1] == "cd":
                if line.split(" ")[2] == "/":
                    current_folder = root_folder
                    continue

                if line.split(" ")[2] == "..":
                    current_folder = current_folder.get_parent()
                    continue

                for child in current_folder.get_children():
                    if child.get_name() == line.split(" ")[2]:
                        current_folder = child
                        continue
                continue

            if line.split(" ")[1] == "ls":
                continue

        if line.split(" ")[0] == "dir":
            current_item = Folder(line.split(" ")[1], current_folder)
            current_folder.add_child(current_item)
            continue

        if line.split(" ")[0].isdigit():
            current_item = File(line.split(" ")[1], current_folder, line.split(" ")[0])
            current_folder.add_child(current_item)
            continue
        
        exit("UNKNOWN INSTRUCTION: " + line)

    return root_folder

def browse_tree(tree: Folder):
    size_sum = 0

    for item in tree.get_children():
        if isinstance(item, Folder):
            if item.get_size() <= 100000:
                size_sum += item.get_size()

            size_sum += browse_tree(item)

    return size_sum

main()
