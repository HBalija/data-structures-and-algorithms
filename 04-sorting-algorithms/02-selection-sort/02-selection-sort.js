const swap = (arr, idx1, idx2) => {
  const temp = arr[idx1];
  arr[idx1] = arr[idx2];
  arr[idx2] = temp;
};

const selectionSort = arr => {

  for (let i = 0; i < arr.length; i++) {
    let min = i;
    for (let j = i + 1; j < arr.length; j++) {
      if (arr[j] < arr[min]) min = j;
    }
    if (min !== i) swap(arr, i, min);
  }
  return arr;
};


console.log(selectionSort([6, 4, 15, 10]));  // [ 4, 6, 10, 15 ]
console.log(selectionSort([7, 1, 2, 3, 4, 5, 6, 8]));  // [1, 2, 3, 4, 5, 6, 7, 8]
