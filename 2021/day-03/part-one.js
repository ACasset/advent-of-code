function execute( input ) {
    let lines = input.split("\n");
				
    let sums = Array.apply(null, Array(lines[0].length)).map(function (x, i) { return 0; });
    let gammaRate = Array.apply(null, Array(lines[0].length)).map(function (x, i) { return 0; });
    let epsilonRate = Array.apply(null, Array(lines[0].length)).map(function (x, i) { return 0; });

    for (var i = 0; i < lines.length; i++) {
        for (var j = 0; j < lines[i].length; j++) {
            sums[j] += parseInt(lines[i][j]);
        }
    }

    for (var i = 0; i < lines[0].length; i++) {
        if (sums[i] > (lines.length / 2)) {
            gammaRate[i] = 1;
            epsilonRate[i] = 0;
        } else {
            gammaRate[i] = 0;
            epsilonRate[i] = 1;
        }
    }

    let powerConsumption = parseInt(gammaRate.join(""), 2) * parseInt(epsilonRate.join(""), 2);

    return powerConsumption;
}