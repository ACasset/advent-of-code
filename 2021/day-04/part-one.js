function execute( input ) {
    let draws = input.slice()[0].split(",");
    let grids = input.splice(1);
    
    for (var i = 0; i < grids.length; i++) {
        grids[i] = grids[i].split("\n");
        
        for (var j = 0; j < grids[i].length; j++) {
            grids[i][j] = grids[i][j].replace(/\s+/g, " ").trim().split(" ");
        }
    }
    
    // Create grids
    
    let bingoGrids = [];
    
    for (var i = 0; i < grids.length; i++) {
        bingoGrids.push( new BingoGrid( grids[i] ));
    }
    
    // Draw
    
    for (var i = 0; i < draws.length; i++) {
        for (var j = 0; j < bingoGrids.length; j++) {
            bingoGrids[j].draw( draws[i] );
        }
        
        if ( i >= 5 ) {
            for (var j = 0; j < bingoGrids.length; j++) {
                if ( bingoGrids[j].isComplete() ) {
                    let sum = 0;
                    
                    for (var k = 0; k < bingoGrids[j].grid.length; k++) {
                        for (var l = 0; l < bingoGrids[j].grid[k].length; l++) {
                            if (bingoGrids[j].grid[k][l].drawn === false) {
                                sum += parseInt(bingoGrids[j].grid[k][l].number);
                            }
                        }
                    }

                    return sum * draws[i];
                }
            }
        }
    }
}

class BingoGrid {
    constructor( grid ) {
        this.grid = grid;
        
        for (var i = 0; i < this.grid.length; i++) {
            for (var j = 0; j < this.grid[i].length; j++) {
                this.grid[i][j] = new BingoNumber( this.grid[i][j] );
            }
        }
    }
    
    draw( number ) {
        for (var i = 0; i < this.grid.length; i++) {
            for (var j = 0; j < this.grid[i].length; j++) {
                if (this.grid[i][j].number === number) {
                    this.grid[i][j].drawn = true;
                    return;
                }
            }
        }
    }
    
    isComplete() {
        // Test des combinaisons horizontales
        for (var i = 0; i < this.grid.length; i++) {
            let isComplete = true;
            
            for (var j = 0; j < this.grid[i].length; j++) {
                if ( this.grid[i][j].drawn === false ) {
                    isComplete = false;
                }
            }
            
            if ( isComplete ) 
                return isComplete;
        }
        
        // Test des combinaisons verticales
        for (var i = 0; i < this.grid.length; i++) {
            let isComplete = true;
            
            for (var j = 0; j < this.grid[i].length; j++) {
                if (this.grid[j][i].drawn === false) {
                    isComplete = false;
                }
            }
            
            if ( isComplete )
                return isComplete;
        }
        
        return false;
    }
}

class BingoNumber {
    constructor( n ) {
        this.number = n;
        this.drawn = false;
    }
}