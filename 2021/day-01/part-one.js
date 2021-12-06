function execute( input ) {
    let lines = input.split("\n");

    let output = 0;

    for (var i = 0; i < (lines.length - 1); i++) {
        if (parseInt(lines[i]) < parseInt(lines[i+1]))
            output++;
    }

    return output;
}