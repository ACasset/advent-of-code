'''Find the highest sum among line-separated groups'''

BASE_PATH = "/workspaces/AdventOfCode/2022/day-"
DAY = "01"
INPUT_TYPE = "real"

def main():
    '''Main function'''
    input_file = read_file()

    current_sum = 0
    highest_sum = -1

    for line in input_file.split("\n"):
        if line:
            current_sum += int(line)
        else:
            highest_sum = max(highest_sum, current_sum)
            current_sum = 0

    print(highest_sum)

def read_file():
    '''Reads input from a file'''
    file = open(BASE_PATH + DAY + "/input_" + INPUT_TYPE + ".txt", "r", encoding="utf-8")
    return file.read()

main()
