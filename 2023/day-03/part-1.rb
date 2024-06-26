def is_number?(char)
    char.match?(/[[:digit:]]/)
end

def is_symbol?(char)
    char.match?(/\#$%&*+\-\/=@]/)
end

def find_numbers(map, line_index)
    line = map[line_index]
    numbers = []
    number = ""
    number_start_index = 0

    (0..line.length-1).each { |i|
        if is_number?(line[i])
            number_start_index = i
            number += line[i]
        else
            unless number.empty?
                if has_symbol_around?(map, line_index, number_start_index, i-1)
                    numbers.push(number.to_i)
                end
            end
        end
    }

    return numbers
end

def has_symbol_around?(map, line_index, column_start_index, column_end_index)
    low_x_range = [0, column_start_index-1].max
    high_x_range = [column_end_index+1, map[0].length-1].min
    low_y_range = [0, line_index-1].max
    high_y_range = [line_index+1, map.length-1].min

    puts "Range will be from #{low_x_range},#{low_y_range} to #{high_x_range},#{high_y_range}"

    (low_y_range..high_y_range).each { |i|
        (low_x_range..high_x_range).each { |j|
            if is_symbol?(map[i][j])
                return true
            end
        }
    }

    return false
end

map = get_input_lines()
sum = 0

(0..map.length-1).each { |i|
    sum += find_numbers(map, i)

    #(0..map[i].length-1).each { |j|
    #    
    #    if has_symbol_around?(map)
    #    puts "Looking at #{j},#{i}: #{map[i][j]}"
    #}
}

puts sum
