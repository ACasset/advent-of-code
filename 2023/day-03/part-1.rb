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

has_symbol_around?(get_input_lines(), 0, 0)
has_symbol_around?(get_input_lines(), 9, 9)

sum = 0
get_input_lines().each { |line|
    #sum += has_symbol_around(line)
}

puts sum
