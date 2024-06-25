def parse_line(line)
    parsing = line.scan(/Game (\d+): (\d+ (red|green|blue);?)+/)
    game_id = parsing.first

    p parsing
    puts
    puts "Game ID: " + game_id
    puts "Game data:"
    return game_id
end

target = { "red" => 12, "green" => 13, "blue" => 14 }

sum = 0
get_input_lines().each { |line|
    sum += parse_line(line)
}

puts sum
