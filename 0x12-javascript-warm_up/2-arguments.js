#!/usr/bin/node

const process = require('process');
if (process.argv.length == 0 || process.argv.length == 1){
        console.log('No argument');
}else if (process.argv.length == 3){
        console.log('Argument found');
}else {
        console.log('Arguments found');
}
