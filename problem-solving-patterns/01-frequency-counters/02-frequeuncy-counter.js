/*

Write a function called isSame, which accepts two arrays.
The function should return true if every value in the array
has its corresponding value squared in the second
array. The frequency of values must be the same.

isSame([1, 2, 3], [4, 1, 9]) // true
isSame([1, 2, 3], [1, 9]) // false
isSame([1, 2, 1], [4, 4, 1]) // false (must be same freqquency)

*/

// Naive approach - O(n**2)

function isSame(arr1, arr2) {
  if (arr1.length !== arr2.length) {
    return false;
  }
  for (let i = 0; i < arr1.length; i++) {
    // searching the index of array 2 with value of array 1 squared
    // indexOf --> O(n)
    const correctIndex = arr2.indexOf(arr1[i] * arr1[i]); // arr1[i] ** 2
    // isn't in array 2
    if (correctIndex === -1) {
      return false;
    }
    // remove element from array 2
    arr2.splice(correctIndex, 1);
  }
  return true;
}

console.log('NAIVE');
console.log(isSame([1, 2, 3], [4, 1, 9])); // true
console.log(isSame([1, 2, 3], [1, 9]));  // false
console.log(isSame([1, 2, 1], [4, 4, 1])); // false


// Better approach - O(n)

function isSameImproved(arr1, arr2) {
  if (arr1.length !== arr2.length) {
    return false;
  }

  const frequencyCounter1 = {};
  const frequencyCounter2 = {};

  for (const val of arr1) {
    // set a key to 1, or add 1 to existing key
    frequencyCounter1[val] = (frequencyCounter1[val] || 0) + 1;
  }

  for (const val of arr2) {
    frequencyCounter2[val] = (frequencyCounter2[val] || 0) + 1;
  }

  for (const key in frequencyCounter1) {
    // return false if key from frequencyCounter1 isn't equal to key squared in frequencyCounter2
    if (!(key * key in frequencyCounter2)) {
      return false;
    }
    // return false if values of these keys aren't the same
    if (frequencyCounter2[key * key] !== frequencyCounter1[key]) {
      return false;
    }
  }
  return true;
}

console.log('IMPROVED');
console.log(isSameImproved([1, 2, 3], [4, 1, 9]));  // true
console.log(isSameImproved([1, 2, 3], [1, 9]));  // false
console.log(isSameImproved([1, 2, 1], [4, 4, 1]));  // false
