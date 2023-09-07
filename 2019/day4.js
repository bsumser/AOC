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
        if (checkInc(i)) {
            ans++;
        }
    }
    return ans;
}

function checkInc(num) {
    var digits = num.toString().split('');
    var realDigits = digits.map(Number);
    var checkSet = new Set(realDigits);

    var check = -1;

    for (let i = 0; i < realDigits.length - 1; i++) {
        if (realDigits[i] > realDigits[i+1])
            return false;
        if ((realDigits[i] == realDigits[i+1]))
            check = 1;
    }

    if (check == 1) {
        return true;
    }
    return false;
}

function checkInc2(num) {
    var digits = num.toString().split('');
    var realDigits = digits.map(Number);
    var checkSet = new Set(realDigits);

    var check = -1;

    for (let i = 0; i < realDigits.length - 1; i++) {
        if (realDigits[i] > realDigits[i+1])
            return false;
        if ((realDigits[i] == realDigits[i+1]) && (realDigits[i] != realDigits[i-1]) && (realDigits[i] != realDigits[i+2]))
            check = 1;
    }

    if (check == 1) {
        return true;
    }
    return false;
}

function part2() {
    let start = 172851;
    let end = 675869;
    let ans = 0;

    for (let i = start; i < end; i++) {
        if (checkInc2(i)) {
            ans++;
        }
    }
    return ans;
}


console.log(part1());
console.log(part2());
