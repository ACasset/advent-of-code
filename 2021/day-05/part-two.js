function execute( input ) {
	let lines = input.split("\n");
	let maxDimension = 0;
	
	lines.forEach(function(line, lineIndex) {
		lines[lineIndex] = line.split(" -> ");
		
		lines[lineIndex].forEach(function(coord, coordIndex) {
			lines[lineIndex][coordIndex] = coord.split(",");
			
			maxDimension = Math.max(maxDimension, lines[lineIndex][coordIndex][0], lines[lineIndex][coordIndex][1]); 
		});
	});
	
	let array = [];
	
	for (var i = 0; i <= maxDimension; i++) {
		array[i] = [];
		
		for (var j = 0; j <= maxDimension; j++) {
			array[i][j] = 0;
		}
	}
	
	lines.forEach(function(line) {
		if (line[0][0] == line[1][0]) {
			// Draw vertical line
			let index = parseInt(line[0][0]);
			let startIndex = Math.min(parseInt(line[0][1]), parseInt(line[1][1]));
			let endIndex = Math.max(parseInt(line[0][1]), parseInt(line[1][1]));
			
			for (var i = startIndex; i <= endIndex; i++) {
				array[i][index]++;
			}
		} else if (line[0][1] == line[1][1]) {
			// Draw horizontal line
			let index = parseInt(line[0][1]);
			let startIndex = Math.min(parseInt(line[0][0]), parseInt(line[1][0]));
			let endIndex = Math.max(parseInt(line[0][0]), parseInt(line[1][0]));
			
			for (var i = startIndex; i <= endIndex; i++) {
				array[index][i]++;
			}
		} else {			
			// Draw diagonal lines
			if (parseInt(line[0][0]) < parseInt(line[1][0]) && parseInt(line[0][1]) < parseInt(line[1][1])) {
				antislashLine(array, line[0], line[1]);
			} else if (parseInt(line[0][0]) < parseInt(line[1][0]) && parseInt(line[0][1]) > parseInt(line[1][1])) {
				slashLine(array, line[0], line[1]);
			} else if (parseInt(line[0][0]) > parseInt(line[1][0]) && parseInt(line[0][1]) < parseInt(line[1][1])) {
				slashLine(array, line[1], line[0]);
			} else if (parseInt(line[0][0]) > parseInt(line[1][0]) && parseInt(line[0][1]) > parseInt(line[1][1])) {
				antislashLine(array, line[1], line[0]);
			}
		}
	});
	
	let count = 0;
	
	array.forEach(function(line) {
		line.forEach(function(column) {
			if (column >= 2)
				count++;
		});
	});
	
	return count;
}

function slashLine(array, start, end) {
	for (var i = parseInt(start[0]), j = parseInt(start[1]); i <= parseInt(end[0]); i++, j--) {
		array[j][i]++;
	}
}

function antislashLine(array, start, end) {
	for (var i = parseInt(start[0]), j = parseInt(start[1]); i <= parseInt(end[0]); i++, j++) {
		array[j][i]++;
	}
}