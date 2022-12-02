'''Collection of useful functions'''

BASE_PATH = "/workspaces/AdventOfCode/2022/day-"

def read_file(day, input_type):
    '''Reads input from a file'''
    file = open(BASE_PATH + day + "/input_" + input_type + ".txt", "r", encoding="utf-8")
    return file.read()
