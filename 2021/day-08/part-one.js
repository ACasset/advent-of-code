function execute( input ) {
    let lines = input.split("\n");
	
	let wantedResults = [2, 3, 4, 7];
	let sum = 0;
	
	lines.forEach(function(line) {
		line = line.replace("\r", "");
		
		let controlDigits = line.split(" | ")[0].split(" ");
		let outputDigits = line.split(" | ")[1].split(" ");
		
		outputDigits.forEach(function(outputDigit) {
			if (wantedResults.includes(outputDigit.length))
				sum++;
		});
	});
	
	return sum;
}