def has_symbol_around?(map, x, y)
    puts "Starting point is: #{x},#{y}"

    low_x_range = x-1
    high_x_range = x+1
    low_y_range = y-1
    low_y_range = y+1

    i in ([0, low_y_range].max)..([map.length, low_y_range].min) do
        j in [0, low_x_range].max..[map[i].length, high_x_range].min do
            puts "Looking at #{j},#{i}: #{map[j][i]}"
        end
    end

    return false
end

def parse_line(line)
    target = { "red" => 12, "green" => 13, "blue" => 14 }

    parsing = line.scan(/^Game (\d+): ([\d\w ,;]+)$/).flatten
    game_id = parsing.first
    game_data = parsing.last
    draws = game_data.split("; ")

    draws.each { |draw|
        groups = draw.split(", ")

        groups.each { |group|
            color = group.split(" ").last

            if (group.split(" ").first.to_i > target[color])
                return 0
            end
        }
    }

    return game_id.to_i
end

has_symbol_around(get_input_lines(), 2, 3)

sum = 0
get_input_lines().each { |line|
    #sum += has_symbol_around(line)
}

puts sum
