def is_winning_number?(number, winning_numbers)
    winning_numbers.include?(number)
end

def get_card_value(line)
    value = 0

    card_index, card_numbers = line.split(": ")
    numbers, winning_numbers = card_numbers.split(" | ")
    winning_numbers = winning_numbers.split(" ")

    # puts "Looking for #{card_index}"
    
    numbers.split(" ").each { |number|
        # puts "Checking if #{number} is a winning number"
        if is_winning_number?(number, winning_numbers)
            # puts "Yes, it's a winning number!"
            unless value == 0
                value *= 2
            else
                value = 1
            end

            # puts "New card value: #{value}"
        end
    }

    value
end

map = get_input_lines()
sum = 0

(0..map.length-1).each { |i|
    sum += get_card_value(map[i])
}

puts sum
