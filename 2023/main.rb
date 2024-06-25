arguments = ARGV

if arguments.length >= 1
    day = arguments[0]
else
    puts "Select a day:"
    day = gets.chomp
end

# TODO: make the variable on 2 digits
# TODO: check if the day exists as a folder

if arguments.length >= 2
    part = arguments[1]
else
    puts "Select a part:"
    part = gets.chomp
end

# TODO: check if the part exists as a file

if arguments.length >= 3
    input = arguments[2]
else
    default_input = "real"
    puts "Select an input [#{default_input}]:"
    # TODO: list the available inputs
    input = gets.chomp

    # TODO: check if user returned something, and use default if not
end

# TODO: check if the input exists as a file

input_file = File.read("day-" + day + "/input-" + input + ".txt")
input_lines = file.split("\n")

require_relative "day-" + day + "/part-" + part
