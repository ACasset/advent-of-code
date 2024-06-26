def is_number?(char)
    return char.match?(/[[:digit:]]/)
end

def is_symbol?(char)
    return char.match?(/[!"\#$%&'()*+,\-/:;<=>?@\[\\\]^_`{|}~]/)
end

def find_numbers(line)
    numbers = []

    (0..line.length-1).each { |i|
        puts "Character: #{line[i]}"
        number = ""

        if is_number?(line[i])
            number += line[i]
        else
            if !number.empty?
                puts "Adding number: #{number}"
                numbers.push(number)
                number = ""
            end
        end
    }

    return numbers
end

def has_symbol_around?(map, x, y)
    puts "Starting point is: #{x},#{y}"

    low_x_range = [0, x-1].max
    high_x_range = [x+1, map[0].length-1].min
    low_y_range = [0, y-1].max
    high_y_range = [y+1, map.length-1].min

    puts "Range will be from #{low_x_range},#{low_y_range} to #{high_x_range},#{high_y_range}"

    (low_y_range..high_y_range).each { |i|
        (low_x_range..high_x_range).each { |j|
            puts "Looking at #{j},#{i}: #{map[i][j]}"
        }
    }

    return false
end

map = get_input_lines()
sum = 0

(0..map.length-1).each { |i|
    puts "Looking for line #{i}: #{map[i]}"
    numbers = find_numbers(map[i])

    puts "Numbers for line #{i}: #{numbers}"

    #(0..map[i].length-1).each { |j|
    #    
    #    if has_symbol_around?(map)
    #    puts "Looking at #{j},#{i}: #{map[i][j]}"
    #}
}

puts sum
