function execute( input ) {
    let lines = input.split("\n");
	
	lines.forEach(function(line, y) {
		lines[y] = line.split("");
		lines[y].forEach(function(value, x) {
			if (value == 9)
				lines[y][x] = true;
			else
				lines[y][x] = false;
		});
	});
	
	let unexploredCount = countUnexplored(lines);
	let basinsSizes = [];
	
	for (var y = 0; y < lines.length; y++) {
		for (var x = 0; x < lines[y].length; x++) {
			if (!lines[y][x]) {
				exploreBasin(lines, y, x);
				let currentUnexploredCount = countUnexplored(lines);
				basinsSizes.push( parseInt(unexploredCount - currentUnexploredCount));
				unexploredCount = currentUnexploredCount;
			}
		}
	}
	
	basinsSizes = basinsSizes.sort(function compare(a, b) {
		return a - b;
	});
	
	let basinsCount = basinsSizes.length;
	
	return basinsSizes[basinsCount-1] * basinsSizes[basinsCount-2] * basinsSizes[basinsCount-3];
}

function countUnexplored(lines) {
	let count = 0;
	
	for (var y = 0; y < lines.length; y++) {
		for (var x = 0; x < lines[y].length; x++) {
			if (!lines[y][x])
				count++;
		}
	}
	
	return count;
}

function exploreBasin(lines, y, x) {
	if (y < 0 || y >= lines.length)
		return;
	
	if (x < 0 || x >= lines[y].length)
		return;
	
	if (lines[y][x])
		return;
	
	lines[y][x] = true;
	
	exploreBasin(lines, y-1, x);
	exploreBasin(lines, y+1, x);
	exploreBasin(lines, y, x-1);
	exploreBasin(lines, y, x+1);
}