function execute( input ) {
	class Cave {
		isBigCave = false;
		visits = 0;
		links = [];
		
        constructor( name ) {
			if ( name === name.toUpperCase() )
				this.isBigCave = true;
        }
		
		addLink( link ) {
			if ( !this.links.includes( link ) )
				this.links.push( link );
		}
    }
    
	let lines = input.split("\n");
	let caves = {};
	
	// Build cave network
	lines.forEach(function(line) {
		let values = line.split("-");
		
		if (typeof(caves[values[0]]) === "undefined") {
			caves[values[0]] = new Cave( values[0] );
		}
		
		if (typeof(caves[values[1]]) === "undefined") {
			caves[values[1]] = new Cave( values[1] );
		}
		
		caves[values[0]].addLink( values[1] );
		caves[values[1]].addLink( values[0] );
	});
	
	console.log(caves);
	
	return exploreCave( caves, "start", "start" );
}

function exploreCave( caves, caveName ) {
	if ( caveName === "end" )
		return 1;
	
	caves[caveName].visits++;
	
	let hasExit = false;
	let validPaths = 0;
	
	caves[caveName].links.forEach(function( linkName ) {
		if ( caves[linkName].isBigCave || caves[linkName].visits == 0 ) {
			hasExit = true;
			validPaths += exploreCave( JSON.parse(JSON.stringify(caves)), linkName );
		}
	});
	
	if ( !hasExit )
		return 0;
	
	return validPaths;
}