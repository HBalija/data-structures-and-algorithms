const merge = (arr1, arr2) => {
  // helper function that merges sorted arrays
  const results = [];
  let i = 0;
  let j = 0;

  while (i < arr1.length && j < arr2.length) {
    if (arr1[i] <= arr2[j]) {
      results.push(arr1[i]);
      i++;
    } else {
      results.push(arr2[j]);
      j++;
    }
  }

  // append remaining values of arr1 or arr2
  while (i < arr1.length) {
    results.push(arr1[i]);
    i++;
  }

  while (j < arr2.length) {
    results.push(arr2[j]);
    j++;
  }

  return results;
};

const mergeSort = (arr) => {
  if (arr.length <= 1) return arr;

  // split array in two parts until base condition is met
  const mid = Math.floor(arr.length / 2);
  const left = mergeSort(arr.slice(0, mid));
  const right = mergeSort(arr.slice(mid));

  // merge sorted arrays
  return merge(left, right);
};


console.log(mergeSort([10, 25, 76, 73, 72, 1, 8])); // [ 1, 8, 10, 25, 72, 73, 76 ]
