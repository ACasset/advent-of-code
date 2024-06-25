def get_input()
    return File.read("day-" + ENV['day'] + "/input-" + ENV['input'] + ".txt")
end

def get_input_lines()
    return get_input().split("\n")
end
