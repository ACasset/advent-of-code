def is_number?(char)
    char.match?(/\d/)
end

def is_symbol?(char)
    char.match?(/\*/)
end

def find_symbols(map, line_index)
    line = map[line_index]
    numbers = []
    sum = 0

    (0..line.length-1).each { |i|
        if is_symbol?(line[i])
            numbers = find_numbers_around(map, line_index, i)

            puts "Found #{numbers.length} numbers on line #{line_index} around index #{i} : #{numbers}"

            if (numbers.length == 2)
                puts "Adding #{numbers[0] * numbers[1]} to the sum"
                sum += numbers[0] * numbers[1]
            end
        end
    }

    return sum
end

def find_complete_number(map, line_index, number_index)
    # puts "Trying to find a complete number at line #{line_index} and index #{number_index}"
    
    left_limit = number_index
    right_limit = number_index
    
    loop do
        i = left_limit - 1
        
        if i < 0 or not is_number?(map[line_index][i])
            break
        end

        left_limit = i
    end

    
    loop do
        j = right_limit + 1
        
        if j >= map[line_index].length or not is_number?(map[line_index][j])
            break
        end

        right_limit = j
    end

    # Assemble number
    number = ""
    (left_limit..right_limit).each { |k|
        number += map[line_index][k]
    }

    puts "Number found = #{number.to_i}"
    
    return number.to_i
end

def find_numbers_around(map, line_index, symbol_index)
    numbers_around = []
    
    low_x_range = [0, symbol_index-1].max
    high_x_range = [symbol_index+1, map[0].length-1].min
    low_y_range = [0, line_index-1].max
    high_y_range = [line_index+1, map.length-1].min

    # We check directly up and down first
    
    if is_number?(map[high_y_range][symbol_index])
        numbers_around.push(find_complete_number(map, high_y_range, symbol_index))
        
        # Alter the range
        high_y_range -= 1
    end
    
    if is_number?(map[low_y_range][symbol_index])
        numbers_around.push(find_complete_number(map, low_y_range, symbol_index))
        
        # Alter the range
        low_y_range += 1
    end

    (low_y_range..high_y_range).each { |i|
        (low_x_range..high_x_range).each { |j|
            if is_number?(map[i][j])
                numbers_around.push(find_complete_number(map, i, j))
            end
        }
    }

    return numbers_around
end

map = get_input_lines()
sum = 0

(0..map.length-1).each { |i|
    sum += find_symbols(map, i)
}

puts sum
