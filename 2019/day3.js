var fs = require('fs');
var filepath = './day2.txt';

function getInput() {
    var dataSplit = fs.readFileSync(filepath).toString('utf8');
    dataSplit = dataSplit.split(/\r?\n?,/);
    
    return 0;
}

function part1(dataSplit) {
    return 0;
}


function part2(dataSplit) {
    return 0;
}

var dataSplit = getInput();

console.log(part1());

console.log(part2());
