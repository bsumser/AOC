var fs = require('fs');
var filepath = './day25.txt';

function getInput() {
    var dataSplit = fs.readFileSync(filepath).toString('utf8');
    dataSplit = dataSplit.split(/\r?\n?/);

    return dataSplit;
}

function part1() {
    var dataSplit = getInput();
    var ans = 0;
    return ans;
}

function part2() {
    var dataSplit = getInput();
    var ans = 0;
    return ans;
}

console.log(part1());
console.log(part2());