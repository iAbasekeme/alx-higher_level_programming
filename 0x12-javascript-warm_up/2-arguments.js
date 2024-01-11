#!/usr/bin/node

const process = require('process');
if (process.argv == 1 || process.argv == 2){
        console.log('No argument');
}else if (process.argv == 3){
        console.log('Argument found');
}else {
        console.log('Arguments found');
}
