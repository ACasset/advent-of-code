def compute_location(steps, seed)
    steps.each { |step, step_data|
        step_data.each { |step_line|
            if seed.between?(step_line[1], step_line[1]+step_line[2])
                seed = seed - step_line[1] + step_line[0]
                break
            end
        }
    }

    seed
end

map = get_input_lines()

seeds = []
steps = {}

current_step = 0

map.each { |line|
    if line.start_with?("seeds:")
        seeds = line[7..-1].split.map(&:to_i)
        next
    end

    if line.include?("map:")
        current_step = (current_step.to_i + 1).to_s
        steps[current_step.to_sym] = []
        next
    end

    steps[current_step.to_sym].push(line.split.map(&:to_i)) unless line.empty?
}

locations = []
seeds.each { |seed| locations.push(compute_location(steps, seed)) }
puts locations.min
