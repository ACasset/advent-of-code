def is_winning_number?(number, winning_numbers)
    winning_numbers.include?(number)
end

def parse_card(map, line_index, quantities)
    card_index, card_numbers = map[line_index].split(": ")
    numbers, winning_numbers = card_numbers.split(" | ")
    winning_numbers = winning_numbers.split(" ")

    cards_to_add = 0
    quantities_index = line_index
    numbers.split(" ").each { |number|
        if is_winning_number?(number, winning_numbers)
            quantities_index += 1
            quantities[quantities_index] += (1 * quantities[line_index])
        end
    }

    return quantities
end

map = get_input_lines()
quantities = Array.new(map.length, 1)
sum = 0
# p quantities

(0..map.length-1).each { |i|
    parse_card(map, i, quantities)
    # p quantities
}

puts quantities.sum
