function execute( input ) {
    let crabs = input.split(",");

    let maxIndex = 0;

    for (var i = 0; i < crabs.length; i++) {
        if (maxIndex < crabs[i]) {
            maxIndex = crabs[i];
        }
    }

    let bestCost = 99999999999999;
    let bestCostIndex = -1;

    for (var i = 0; i <= maxIndex; i++) {
        let currentCost = 0;

        for (var j = 0; j < crabs.length; j++) {
            let distance = Math.abs(crabs[j] - i);

            for (var k = distance; k > 0; k--) {
                currentCost += k;
            }
        }

        if (currentCost < bestCost) {
            bestCost = currentCost;
            bestCostIndex = i;
        }
    }

    return bestCost;
}