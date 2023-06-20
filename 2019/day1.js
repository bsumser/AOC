const { performance } = require('perf_hooks');
var fs = require('fs')
var filepath = './day1.txt'

var dataSplit = fs.readFileSync(filepath).toString('utf8');
dataSplit = dataSplit.split(/\r?\n/);

const tailRecurHelper = (mass, fuelAcc) => {
    mass = (Math.floor(mass / 3) - 2)
    if (mass <= 0) {
        return fuelAcc
    }

    else {
        return fuelAcc += mass + tailRecurHelper(mass, fuelAcc)
    }
}

const recurHelper = (mass, fuelAcc) => {
    mass = (Math.floor(mass / 3) - 2)
    if (mass <= 0) {
        return fuelAcc
    }

    else {
        return recurHelper(mass)
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
    var startTime = performance.now()
    var fuel = 0

    for (let i = 0; i < dataSplit.length; i++) {
        fuel += tailRecurHelper(parseInt(dataSplit[i], 10), 0)
    }
    var endTime = performance.now()
    console.log(`Call to part2 took ${endTime - startTime} milliseconds`)
    return fuel
}

console.log(part1())
console.log(part2())