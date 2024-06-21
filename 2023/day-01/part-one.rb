input = "real"

file = File.read("input-" + input + ".txt")
lines = file.split("\n")

def find_number(line)
    numbers = line.scan(/\d/)
    return (numbers.first + numbers.last).to_i
end

sum = 0
lines.each { |line|
    sum += find_number(line)
}

puts sum
