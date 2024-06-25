def parse_line(line)
    draw_composition = { "red" => 0, "green" => 0, "blue" => 0 }

    parsing = line.scan(/^Game (\d+): ([\d\w ,;]+)$/).flatten
    game_id = parsing.first
    game_data = parsing.last
    draws = game_data.split("; ")

    draws.each { |draw|
        groups = draw.split(", ")

        groups.each { |group|
            color = group.split(" ").last

            if (group.split(" ").first.to_i > draw_composition[color])
                draw_composition[color] = group.split(" ").first.to_i
            end
        }
    }

    return draw_composition["red"] * draw_composition["green"] * draw_composition["blue"]
end

sum = 0
get_input_lines().each { |line|
    sum += parse_line(line)
}

puts sum
