function execute( input ) {
    let lines = input.split("\n");
	
	let scores = [];
	
	lines.forEach(function(line) {
		let expected = [];
		let characters = line.split("");
		
		for (var i = 0; i < characters.length; i++) {
			switch (characters[i]) {
				// Opening
				
				case "(":
					expected.push(")");
				break;
				
				case "[":
					expected.push("]");
				break;
				
				case "{":
					expected.push("}");
				break;
				
				case "<":
					expected.push(">");
				break;
				
				// Closing
				
				case ")":
				case "}":
				case "]":
				case ">":
					if (expected.pop() != characters[i]) {
						expected = [];
						i = characters.length;
					}
				break;
			}
		}
		
		if (expected.length > 0) {
			expected.reverse();
			let score = 0;
			
			for (var i = 0; i < expected.length; i++) {
				score *= 5;
				
				switch (expected[i]) {
					case ")":
						score += 1;
					break;
					
					case "]":
						score += 2;
					break;
					
					case "}":
						score += 3;
					break;
					
					case ">":
						score += 4;
					break;
				}
			}
			
			scores.push(score);
		}
	});
	
	scores = scores.sort(function compare(a, b) {
		return a - b;
	});
	
	return scores[(scores.length-1)/2];
}