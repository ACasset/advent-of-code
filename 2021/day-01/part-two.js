function execute( input ) {
    let lines = input.split("\n");

    let output = 0;

    let currentSum = parseInt(lines[0]) + parseInt(lines[1]) + parseInt(lines[2]);
    let lastSum = currentSum;

    for (var i = 1; i < (lines.length - 2); i++) {
        currentSum = parseInt(lines[i]) + parseInt(lines[i+1]) + parseInt(lines[i+2]);

        if (lastSum < currentSum)
            output++;

        lastSum = currentSum;
    }

    return output;
}