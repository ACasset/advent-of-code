function execute( input ) {
    let lines = input.split("\n");

    let horizontalPosition = 0;
    let verticalPosition = 0;

    for (var i = 0; i < lines.length; i++) {
        let fields = lines[i].split(" ");
        
        switch (fields[0]) {
            case "forward":
                horizontalPosition += parseInt(fields[1]);
            break;
            
            case "up":
                verticalPosition -= parseInt(fields[1]);
            break;
            
            case "down":
                verticalPosition += parseInt(fields[1]);
            break;
            
            default:
                console.log("ERROR @ line " + i + ": " + lines[i]);
            break;
        }
    }

    return horizontalPosition * verticalPosition;
}