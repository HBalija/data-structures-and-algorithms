/*
Given two strings, write a function to determine if the
second string is an anagram of the first. An anagram is a word, phrase,
or name formed by rearranging the letters of another,
such as cinema, formed from iceman.

validAnagram('', '') // true
validAnagram('aaz, 'zza') // false
validAnagram('anagram', 'nagaram') // true
*/

function validAnagram(str1, str2) {
  // O(n)time
  if (str1.length !== str2.length) {
    return false;
  }

  const charObj = {};

  for (const char of str1) {
    charObj[char] = (charObj[char] || 0) + 1;
  }

  for (const char of str2) {
    if (charObj[char] > 0) {
      charObj[char]--;
    } else {
      return false;
    }
  }

  return true;
}


console.log(validAnagram('', '')); // true
console.log(validAnagram('aaz', 'zza')); // false
console.log(validAnagram('anagram', 'nagaram')); // true
