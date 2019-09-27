function getDigit(num, position) {
  return Math.floor(Math.abs(num) / Math.pow(10, position)) % 10;
}


function countDigits(num) {
  return String(Math.abs(num)).length;
}

function getMostDigits(arr) {

  let mostDigits = 0;
  for (const item of arr) {
    mostDigits = Math.max(mostDigits, countDigits(item));
  }
  return mostDigits;
}

/* END HELPER FUNCTIONS */


const radixSort = arr => {

  const maxDigits = getMostDigits(arr);

  for (let i = 0; i < maxDigits; i++) {

    // const tempArr = [[], [], [], [], [], [], [], [], [], []];
    const tempArr = Array.from({ length: 10 }, () => []);

    for (let j = 0; j < arr.length; j++) {
      const digit = getDigit(arr[j], i);
      tempArr[digit].push(arr[j]);
    }
    arr = [].concat(...tempArr);

  }
  return arr;
};


console.log(radixSort([34, 56, 3456, 234, 0, 1, 63])); // [ 0, 1, 34, 56, 63, 234, 3456 ]
