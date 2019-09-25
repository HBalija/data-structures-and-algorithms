
// Collect all odd values in array

const collectOddValues = arr => {
  const result = [];

  function helper(subArr) {
    // recursive function

    if (!subArr.length) {
      return;
    }
    if (subArr[0] % 2 !== 0) {
      result.push(subArr[0]);
    }

    helper(subArr.slice(1));
  }

  helper(arr);
  return result;
}

console.log(collectOddValues([1, 2, 4, 3, 5, 66, 77, 89])); // [1, 3, 5, 77, 89]
