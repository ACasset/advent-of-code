function execute( input ) {
    let inputSchool = input.split(",");

    let initialSchool = [];

    for (var i = 0; i <= 8; i++) {
        initialSchool[i] = inputSchool.filter(x => x == i).length;
    }

    console.log(initialSchool);

    for (var i = 1; i <= 256; i++) {
        let currentSchool = [];

        for (var j = 0; j <= 8; j++) {
            if (j == 6)
                currentSchool[j] = initialSchool[7] + initialSchool[0];
            else if (j == 8)
                currentSchool[j] = initialSchool[0];
            else
                currentSchool[j] = initialSchool[j+1];
        }

        initialSchool = currentSchool;
    }

    return currentSchoolSum(initialSchool);
}

function currentSchoolSum(school) {
    let sum = 0;

    school.forEach(function(ttl) {
        sum += ttl;
    });

    return sum;
}