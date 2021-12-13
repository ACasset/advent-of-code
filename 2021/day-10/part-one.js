function execute( input ) {
    let lines = input.split("\n");
	
	let causes = { ")": 0, "}": 0, "]": 0, ">": 0 };
	
	lines.forEach(function(line) {
		let expected = [];
		
		line.split("").forEach(function(character) {
			switch (character) {
				// Opening
				
				case "(":
					expected.push(")");
				break;
				
				case "{":
					expected.push("}");
				break;
				
				case "[":
					expected.push("]");
				break;
				
				case "<":
					expected.push(">");
				break;
				
				// Closing
				
				case ")":
				case "}":
				case "]":
				case ">":
					if (expected.pop() != character) {
						causes[character] += 1;
						return;
					}
				break;
			}
		});
	});
	
	return causes[")"] * 3 + causes["]"] * 57 + causes["}"] * 1197 + causes[">"] * 25137;
}