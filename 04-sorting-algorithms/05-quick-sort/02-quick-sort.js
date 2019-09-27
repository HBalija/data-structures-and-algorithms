const swap = (arr, i, j) => {
  const temp = arr[i];
  arr[i] = arr[j];
  arr[j] = temp;
};

const pivot = (arr, start = 0, end = arr.length + 1) => {

  const pivot = arr[start];
  let swapIdx = start;

  for (let i = start + 1; i < arr.length; i++) {
    if (pivot > arr[i]) {
      // increment if arr[i] is smaller than arr[pivot]
      swapIdx++;
      // swap arr[i] with arr[swapIdx]
      swap(arr, swapIdx, i);
    }
  }
  swap(arr, start, swapIdx);

  return swapIdx;
};


const quickSort = (arr, left = 0, right = arr.length - 1) => {

  if (left < right) {

    const pivotIdx = pivot(arr, left);

    quickSort(arr, left, pivotIdx - 1);
    quickSort(arr, pivotIdx + 1, right);
  }
  return arr;
};

console.log(quickSort([9, 4, 8, 2, 100, -3, 1, 5, 7, 6, 3]));
// [ -3, 1, 2, 3, 4, 5, 6, 7, 8, 9, 100 ]
