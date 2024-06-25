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

sum = 0
get_input_lines().each { |line|
    sum += parse_line(line)
}

puts sum
