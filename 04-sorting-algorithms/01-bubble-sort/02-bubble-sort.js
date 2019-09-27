const swap = (arr, idx1, idx2) => {
  const temp = arr[idx1];
  arr[idx1] = arr[idx2];
  arr[idx2] = temp;
};

const bubbleSort = arr => {
  for (let i = arr.length - 1; i > 0; i--) {
    let noSwaps = true;
    for (let j = 0; j < i; j++) {
      if (arr[j] > arr[j + 1]) {
        noSwaps = false;
        swap(arr, j, j + 1);
      }
    }
    if (noSwaps) break;
  }
  return arr;
};


// console.log(bubbleSort([6, 4, 15, 10]));  // [ 4, 6, 10, 15 ]
console.log(bubbleSort([7, 1, 2, 3, 4, 5, 6, 8]));  // [1, 2, 3, 4, 5, 6, 7, 8]
