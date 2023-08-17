var fs = require('fs');
var filepath = './day2.txt';

function getInput() {
    var dataSplit = fs.readFileSync(filepath).toString('utf8');
    dataSplit = dataSplit.split(/\r?\n?,/);

    const input = [172851, 675869]
    return input;
}

function part1(input) {
    for (let i = input[0]; i < input[1]; i++) {

    }
    return 0;
}


function part2(input) {
    return 0;
}

input = getInput();

console.log(part1(input));

console.log(part2(input));
