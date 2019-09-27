const linearSearch = (arr, num) => {
  // return index of element if found

  for (let i = 0; i < arr.length; i++) {
    if (arr[i] === num) return i;
  }
  return -1;
};

console.log(linearSearch([1, 5, 3, 7, 5, 8, 9], 3)); // 2
console.log(linearSearch([1, 5, 3, 7, 5, 8, 9], 6)); // -1
