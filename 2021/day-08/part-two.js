function execute( input ) {
    let lines = input.split("\n");
	
	let wantedResults = [2, 3, 4, 7];
	let sum = 0;
	
	lines.forEach(function(line) {
		line = line.replace("\r", "");
		
		let controlDigits = line.split(" | ")[0].split(" ");
		controlDigits.forEach(function(digit, index) {
			controlDigits[index] = digit.split("");
		});
		
		let outputDigits = line.split(" | ")[1].split(" ");
		outputDigits.forEach(function(digit, index) {
			outputDigits[index] = digit.split("");
		});
		
		let reference = matchDigits(controlDigits);
		let outputNumber = "";
		
		outputDigits.forEach(function(digit) {
			for (var i = 0; i <= 9; i++) {
				if (arrayDiff(digit, reference[i]).length === 0) {
					outputNumber += i;
					break;
				}
			}
		});
		
		sum += parseInt(outputNumber);
	});
	
	return sum;
}

function matchDigits(digits) {
	let matches = {};
	
	matches[1] = digits.filter(x => x.length === 2)[0];
	matches[7] = digits.filter(x => x.length === 3)[0];
	matches[4] = digits.filter(x => x.length === 4)[0];
	matches[8] = digits.filter(x => x.length === 7)[0];
	matches[5] = digits.filter(x => x.length === 5 && arrayInter(x, arrayDiff(matches[4], matches[7])).length === 3)[0];
	matches[9] = digits.filter(x => x.length === 6 && arrayInter(x, arrayUnion(matches[5], matches[1])).length === 6)[0];
	matches[3] = digits.filter(x => x.length === 5 && arrayInter(x, matches[5]).length !== 5 && arrayInter(x, matches[9]).length === 5)[0];
	matches[6] = digits.filter(x => x.length === 6 && arrayInter(x, arrayUnion(matches[5], arrayDiff(matches[3], matches[8]))).length === 6)[0];
	matches[0] = digits.filter(x => x.length === 6 && arrayInter(x, arrayUnion(matches[1], arrayDiff(matches[3], matches[8]))).length === 4)[0];
	matches[2] = digits.filter(x => x.length === 5 && arrayInter(x, arrayDiff(matches[4], matches[8])).length === 3)[0];
	
	return matches;
}

function arrayUnion(array1, array2) {
	let union = [];
	
	array1.forEach(function(item) {
		if (!union.includes(item))
			union.push(item);
	});
	
	array2.forEach(function(item) {
		if (!union.includes(item))
			union.push(item);
	});
	
	return union;
}

function arrayInter(array1, array2) {
	return array1.filter(x => array2.includes(x));
}

function arrayDiff(array1, array2) {
	let union = arrayUnion(array1, array2);
	let inter = arrayInter(array1, array2);
	
	inter.forEach(function(item) {
		if (union.indexOf(item) !== -1)
			union.splice(union.indexOf(item), 1);
	});
	
	return union;
}