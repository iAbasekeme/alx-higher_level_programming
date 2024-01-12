#!/usr/bin/node

const args = process.argv.slice(2).map(Number);
function findSecondLargest(arr) {
  if (arr.length <= 1) {
    return 0;
  }

  let max = arr[0];
  let secondMax = Number.MIN_SAFE_INTEGER;

  for (let i = 1; i < arr.length; i++) {
    if (arr[i] > max) {
      secondMax = max;
      max = arr[i];
    } else if (arr[i] > secondMax && arr[i] !== max) {
      secondMax = arr[i];
    }
  }

  return secondMax;
}
console.log(findSecondLargest(args));
