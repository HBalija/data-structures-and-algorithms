const _hash = (key, arrayLen) => {
  let total = 0;
  const somePrime = 31;
  // max 100 iterations
  for (let i = 0; i < Math.min(key.length, 100); i++) {
    const char = key[i];
    const value = char.charCodeAt(0) - 96;
    total = (total + somePrime + value) % arrayLen;
  }
  return total;
};

console.log(_hash('Hello', 41)); // 11
console.log(_hash('hash_key', 97));  // 33
