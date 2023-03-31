function findFirstNonRepeatingChar(str) {
    const charCount = {};
    for (let i = 0; i < str.length; i++) {
      const char = str[i];
      if (charCount[char]) {
        charCount[char]++;
      } else {
        charCount[char] = 1;
      }
    }
    for (let i = 0; i < str.length; i++) {
      const char = str[i];
      if (charCount[char] === 1) {
        return char;
      }
    }
    return null;
  }

  const str = "abcbdea";
const firstNonRepeatingChar = findFirstNonRepeatingChar(str);
console.log(firstNonRepeatingChar); // Output: "c"
