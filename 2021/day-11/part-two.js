function execute( input ) {
	let lines = input.split("\n");
	
	lines.forEach(function(line, lineIndex) {
		lines[lineIndex] = line.split("");
		
		lines[lineIndex].forEach(function(value, valueIndex) {
			line[lineIndex][valueIndex] = parseInt(value);
		});
	});
	
	let flashes = 0;
	
	for (var step = 1; flashes != 100; step++) {
		flashes = 0;
		
		// Increase all octopuses by 1
		for (var y = 0; y < lines.length; y++) {
			for (var x = 0; x < lines[y].length; x++) {
				lines[y][x]++;
			}
		}
		
		// Flash!
		let flashOccurred = false;
		do {
			flashOccurred = false;
			
			for (var y = 0; y < lines.length; y++) {
				for (var x = 0; x < lines[y].length; x++) {
					if (lines[y][x] >= 10 && lines[y][x] < 999) {
						flashOccurred = true;
						flashes++;
						lines[y][x] = 999;
						
						if (y > 0 && x > 0)
							lines[y-1][x-1]++;
						
						if (y > 0)
							lines[y-1][x]++;
						
						if (y > 0 && x < (lines[y].length - 1))
							lines[y-1][x+1]++;
						
						if (x > 0)
							lines[y][x-1]++;
						
						if (x < (lines[y].length - 1))
							lines[y][x+1]++;
						
						if (y < (lines.length - 1) && x > 0)
							lines[y+1][x-1]++;
						
						if (y < (lines.length - 1))
							lines[y+1][x]++;
					
						if (y < (lines.length - 1) && x < (lines[y].length - 1))
							lines[y+1][x+1]++;
					}
				}
			}
		} while (flashOccurred);
		
		// Reset octopuses that flashed
		for (var y = 0; y < lines.length; y++) {
			for (var x = 0; x < lines[y].length; x++) {
				if (lines[y][x] >= 10)
					lines[y][x] = 0;
			}
		}
	}
	
	return (step - 1);
}