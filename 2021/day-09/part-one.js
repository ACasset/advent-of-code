function execute( input ) {
    let lines = input.split("\n");
	
	lines.forEach(function(line, index) {
		lines[index] = line.split("");
	});
	
	let lowestHeights = [];
	
	for (var y = 0; y < lines.length; y++) {
		for (var x = 0; x < lines[y].length; x++) {
			let currentHeight = lines[y][x];
			
			if (x >= 1 && parseInt(lines[y][x-1]) <= parseInt(currentHeight))
				continue;
			
			if (x < (lines[y].length - 1) && parseInt(lines[y][x+1]) <= parseInt(currentHeight))
				continue;
			
			if (y >= 1 && parseInt(lines[y-1][x]) <= parseInt(currentHeight))
				continue;
			
			if (y < (lines.length - 1) && parseInt(lines[y+1][x]) <= parseInt(currentHeight))
				continue;
			
			lowestHeights.push(currentHeight);
		}
	}
	
	let sum = lowestHeights.length;
	
	lowestHeights.forEach(function(lowestHeight) {
		sum += parseInt(lowestHeight);
	});
	
	return sum;
}