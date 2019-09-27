function sumZero(arr) {
  // Naive solution - O(n**2)time, O(1)space
  for (let i = 0; i < arr.length; i++) {
    for (let j = i + 1; j < arr.length; j++) {
      if (arr[i] + arr[j] === 0) {
        return [arr[i], arr[j]];
      }
    }
  }
}

console.log('NAIVE');
console.log(sumZero([-3, -2, -1, 0, 1, 2, 3])); // [-3, 3]
console.log(sumZero([-2, 0, 1, 3])); // undefined
console.log(sumZero([-2, 0, 1, 2, 3])); // [ -2, 2 ]
console.log(sumZero([-1, 1])); // [ -1, 1 ]


function sumZeroImproved(arr) {
  // Improved solution -  O(n)time, O(1)space

  // starting indexes (first and last)
  let left = 0;
  let right = arr.length - 1;

  while (left < right) {
    const sum = arr[left] + arr[right];

    if (sum === 0) {
      return [arr[left], arr[right]];
    } else if (sum > 0) {
      right--;
    } else {
      left++;
    }
  }
}

console.log('IMPROVED');
console.log(sumZeroImproved([-3, -2, -1, 0, 1, 2, 3])); // [-3, 3]
console.log(sumZeroImproved([-2, 0, 1, 3])); // undefined
console.log(sumZeroImproved([-2, 0, 1, 2, 3])); // [ -2, 2 ]
console.log(sumZeroImproved([-1, 1])); // [ -1, 1 ]
