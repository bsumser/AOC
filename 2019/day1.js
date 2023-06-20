var fs = require('fs')
var filepath = './day1.txt'

var dataSplit = fs.readFileSync(filepath).toString('utf8');
dataSplit = dataSplit.split(/\r?\n/);

const recurHelper = (mass) => {
    if (mass == 0)
    return mass
}
const part1 = () => {
    console.log(dataSplit)
    
    var fuel = 0

    for (let i = 0; i < dataSplit.length; i++) {
        fuel += Math.floor(parseInt(dataSplit[i], 10) / 3) - 2
        //console.log(parseInt(dataSplit[i]))
    }
    return fuel
}

const part2= () => {
    //console.log(dataSplit)
    return 0
}

console.log(part1())
console.log(part2())