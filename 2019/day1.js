var fs = require('fs')
var filepath = './day1.txt'

var dataSplit = fs.readFileSync(filepath).toString('utf8');
dataSplit = dataSplit.split(/\r?\n/);

const recurHelper = (mass, fuelAcc) => {
    mass = (Math.floor(mass / 3) - 2)
    if (mass <= 0) {
        return fuelAcc
    }

    else {
        return fuelAcc += mass + recurHelper(mass, fuelAcc)
    }
}
const part1 = () => {
    //console.log(dataSplit)
    
    var fuel = 0

    for (let i = 0; i < dataSplit.length; i++) {
        fuel += Math.floor(parseInt(dataSplit[i], 10) / 3) - 2
        //console.log(parseInt(dataSplit[i]))
    }
    return fuel
}

const part2 = () => {
    var fuel = 0

    for (let i = 0; i < dataSplit.length; i++) {
        fuel += recurHelper(parseInt(dataSplit[i], 10), 0)
    }
    return fuel
}

console.log(part1())
console.log(part2())