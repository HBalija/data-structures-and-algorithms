/*
FACTORIAL

4! = 4 * 3 * 2 * 1 // 24

3! = 3 * 2!
*/

// Iterative

const factorialIterativly = num => {
  let total = 1;
  for (let i = num; i > 1; i--) {
    total *= i;
  }
  return total;
};

console.log(factorialIterativly(4)); // 24


// Recursive

const factorial = num => {
  if (num === 1) return num;
  return num * factorial(num - 1);
};

console.log(factorial(4)); // 24
