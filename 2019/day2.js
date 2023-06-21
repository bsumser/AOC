var fs = require('fs');
var filepath = './day2.txt';

function getInput() {
    var dataSplit = fs.readFileSync(filepath).toString('utf8');
    dataSplit = dataSplit.split(/\r?\n?,/);

    return dataSplit;
}

function part1() {
    var dataSplit = getInput();
    console.log(dataSplit);
    return 0;
}

function part2() {
    var dataSplit = getInput();
    console.log(dataSplit);
    return 0;
}

console.log(part1());
console.log(part2());