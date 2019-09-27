function maxSubarraySum(arr, num) {
  // Naive approach - O(n**2)time
  if (num > arr.length) {
    return null;
  }

  // iniitial max cannot be zero if we are working with negative numbers
  let max = -Infinity;
  for (let i = 0; i < arr.length - num + 1; i++) {
    let temp = 0;
    for (let j = 0; j < num; j++) {
      temp += arr[i + j];
    }
    if (temp > max) {
      max = temp;
    }
  }
  return max;
}

console.log('NAIVE');
console.log(maxSubarraySum([1, 2, 5, 2, 8, 1, 5], 2)); // 10
console.log(maxSubarraySum([1, 2, 5, 2, 8, 1, 5], 4)); // 17
console.log(maxSubarraySum([4, 2, 1, 6], 1)); // 6
console.log(maxSubarraySum([], 3)); // null


function maxSubarraySumImproved(arr, num) {
  // Better approach - O(n)time
  if (arr.length < num) return null;

  let tempSum = 0;
  let maxSum = 0;

  for (let i = 0; i < num; i++) {
    maxSum += arr[i];
  }

  tempSum = maxSum;

  for (let i = num; i < arr.length; i++) {
    tempSum = tempSum - arr[i - num] + arr[i];
    maxSum = Math.max(maxSum, tempSum);
  }

  return maxSum;
}

console.log('IMPROVED');
console.log(maxSubarraySumImproved([1, 2, 5, 2, 8, 1, 5], 2)); // 10
console.log(maxSubarraySumImproved([1, 2, 5, 2, 8, 1, 5], 4)); // 17
console.log(maxSubarraySumImproved([4, 2, 1, 6], 1)); // 6
console.log(maxSubarraySumImproved([], 3)); // null
