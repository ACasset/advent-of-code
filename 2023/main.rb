arguments = ARGV

if arguments.length >= 1
    ENV['day'] = arguments[0]
else
    puts "Select a day:"
    ENV['day'] = gets.chomp
end

# TODO: make the variable on 2 digits
# TODO: check if the day exists as a folder

if arguments.length >= 2
    ENV['part'] = arguments[1]
else
    puts "Select a part:"
    ENV['part'] = gets.chomp
end

# TODO: check if the part exists as a file

if arguments.length >= 3
    ENV['input'] = arguments[2]
else
    default_input = "real"
    puts "Select an input [#{default_input}]:"
    # TODO: list the available inputs
    ENV['input'] = gets.chomp

    # TODO: check if user returned something, and use default if not
end

# TODO: check if the input exists as a file

require_relative "functions.rb"

require_relative "day-" + ENV['day'] + "/part-" + ENV['part']
