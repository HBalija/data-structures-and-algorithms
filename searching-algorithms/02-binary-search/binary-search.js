
const binarySearch = (arr, num) => {
  // Divide and conquer

  let left = 0;
  let right = arr.length - 1;

  while (left <= right) {
    const mid = Math.floor((left + right) / 2);
    if (num === arr[mid]) return mid;
    else if (num < arr[mid]) right = mid - 1;
    else if (num > arr[mid]) left = mid + 1;
  }
  return -1;
};

console.log(binarySearch([1, 2, 4, 6, 8, 9, 11, 14, 16, 19, 22, 57], 19));  // 9
console.log(binarySearch([1, 4, 5, 6, 8, 9, 10, 12], 3));  // -1
