var fs = require('fs')
var filepath = './day1.txt'

var dataSplit = fs.readFileSync(filepath, 'utf8', function(err, data) {
    if (err) {
        console.error("could not open file: %s", err);
    }
});


const recurHelper = (mass) => {
    if (mass == 0)
    return mass
}
const part1 = () => {
    console.log(dataSplit)
    return 0
}

const part2= () => {
    console.log(dataSplit)
    return 0
}

console.log(part1())
console.log(part2())