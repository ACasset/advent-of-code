def convert(number)
    case number
    when "one" then return 1
    when "two" then return 2
    when "three" then return 3
    when "four" then return 4
    when "five" then return 5
    when "six" then return 6
    when "seven" then return 7
    when "eight" then return 8
    when "nine" then return 9
    else return number
    end
end

def find_number(line)
    numbers = line.scan(/(?=(one|two|three|four|five|six|seven|eight|nine|\d))/).flatten
    return (convert(numbers.first).to_s + convert(numbers.last).to_s).to_i
end

sum = 0
input_lines.each { |line|
    sum += find_number(line)
}

puts sum
