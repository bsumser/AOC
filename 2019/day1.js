var fs = require('fs')
var filepath = './day1.txt'

fs.readFile(filepath, 'utf8', function(err, data) {
    if (err) {
        console.error("could not open file: %s", err);
    }
    console.log(data)
});

const part1 = () => {
    return 0
}

const part2= () => {
    return 0
}

console.log(part1())
console.log(part2())