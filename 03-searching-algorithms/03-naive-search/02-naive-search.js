const naiveSearch = (long, short) => {
  // search how many time substring appears in a string
  let counter = 0;

  for (let i = 0; i < long.length; i++) {
    if (long[i] === short[0]) {
      for (let j = 0; j < short.length; j++) {
        if (short[j] !== long[i + j]) break;
        if (j === short.length - 1) counter++;
      }
    }
  }
  return counter;
};


console.log(naiveSearch('kaboomdboomda', 'boom')); // 2
console.log(naiveSearch('lorie loled', 'lol')); // 1
