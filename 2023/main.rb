arguments = ARGV

if arguments.length >= 1
    ENV["day"] = arguments[0]
else
    print "Select a day: "
    ENV["day"] = STDIN.gets.chomp
end

# TODO: make the variable on 2 digits
# TODO: check if the day exists as a folder

if arguments.length >= 2
    ENV["part"] = arguments[1]
else
    print "Select a part: "
    ENV["part"] = STDIN.gets.chomp
end

# TODO: check if the part exists as a file

if arguments.length >= 3
    ENV["input"] = arguments[2]
else
    default_input = "real"
    print "Select an input [#{default_input}]: "
    # TODO: list the available inputs
    ENV["input"] = STDIN.gets.chomp

    # TODO: check if user returned something, and use default if not
end

# TODO: check if the input exists as a file

require_relative "functions.rb"

require 'benchmark'
performance = Benchmark.measure do
    print "Result: "
    require_relative "day-" + ENV["day"] + "/part-" + ENV["part"]
end
puts "Execution time: " + performance.total.to_s
