let fs = require('fs');
let filepath = './day4.txt';

function getInput() {
    let dataSplit = fs.readFileSync(filepath).toString('utf8');
    dataSplit = dataSplit.split(/\n/);
    
    return dataSplit;
}

function part1() {
    let start = 172851;
    let end = 675869;
    let ans = 0;

    for (let i = start; i < end; i++) {
        
    }
    return ans;
}

function part2() {
    let dataSplit = getInput();
    let ans = 0;
    return dataSplit;
}

console.log(part1());
console.log(part2());