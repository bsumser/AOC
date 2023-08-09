let fs = require('fs');
let filepath = './day1.txt';

function getInput() {
    let dataSplit = fs.readFileSync(filepath).toString('utf8');
    dataSplit = dataSplit.split("\n");

    for (let i = 0; i < dataSplit.length; i++) {
        
    }

    return dataSplit;
}

function part1() {
    let dataSplit = getInput();
    console.log(dataSplit)
    let ans = 0;
    return ans;
}

function part2() {
    let dataSplit = getInput();
    console.log(dataSplit)
    let ans = 0;
    return ans;
}

console.log(part1());
console.log(part2());