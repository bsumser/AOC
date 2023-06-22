var fs = require('fs');
var filepath = './day2.txt';

function getInput() {
    var dataSplit = fs.readFileSync(filepath).toString('utf8');
    dataSplit = dataSplit.split(/\r?\n?,/);
    
    for (let i = 0; i < dataSplit.length; i++) {
        dataSplit = dataSplit.map(Number);
    }

    return dataSplit;
}

function part1() {
    var dataSplit = getInput();
    //the first step is to restore the gravity assist program (your puzzle input) to the "1202 program alarm" 
    //state it had just before the last computer caught fire. 
    //To do this, before running the program, replace position 1 with the value 12 and replace position 2 with the value 2. 
    //What value is left at position 0 after the program halts?
    dataSplit[1] = 12;
    dataSplit[2] = 2;
    //console.log(dataSplit);

    for (let i = 0; i < dataSplit.length; i+=4) {
        switch(dataSplit[i]) {
            case 1: //console.log("add %s + %s, place at %s", dataSplit[i+1], dataSplit[i+2], dataSplit[i+3]);
                dataSplit[dataSplit[i+3]] = dataSplit[dataSplit[i+1]] + dataSplit[dataSplit[i+2]]
                break;

            case 2: //console.log("mult %s * %s, place at %s", dataSplit[i+1], dataSplit[i+2], dataSplit[i+3]);
                dataSplit[dataSplit[i+3]] = dataSplit[dataSplit[i+1]] * dataSplit[dataSplit[i+2]]
                break;
            case 99:
                return dataSplit[0];

            default: //console.log("no case for %s", dataSplit[i]);
                break;
        }
    }
    return dataSplit[0];
}

function part2Helper(dataSplit, i, j) {
    dataSplit[1] = i;
    dataSplit[2] = j;
    //console.log(dataSplit);

    for (let i = 0; i < dataSplit.length; i+=4) {
        switch(dataSplit[i]) {
            case 1: //console.log("add %s + %s, place at %s", dataSplit[i+1], dataSplit[i+2], dataSplit[i+3]);
                dataSplit[dataSplit[i+3]] = dataSplit[dataSplit[i+1]] + dataSplit[dataSplit[i+2]]
                break;

            case 2: //console.log("mult %s * %s, place at %s", dataSplit[i+1], dataSplit[i+2], dataSplit[i+3]);
                dataSplit[dataSplit[i+3]] = dataSplit[dataSplit[i+1]] * dataSplit[dataSplit[i+2]]
                break;
            case 99:
                return dataSplit[0];

            default: //console.log("no case for %s", dataSplit[i]);
                break;
        }
    }
    return dataSplit[0];
}

function part2() {
    for (let i = 0; i < 100; i++) {
        for (let j = 0; j < 100; j++) {
            var dataSplit = getInput();
            if (19690720 == part2Helper(dataSplit, i, j)) {
                return 100 * i + j;
            }
        }

    }
    return 0;
}

console.log(part1());
console.log(part2());