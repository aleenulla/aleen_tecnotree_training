function reverseWords(str) {
    // Split the string into an array of words
    const wordsArr = str.split(" ");
    // Reverse the array
    wordsArr.reverse();
    // Join the array into a string
    const reversedStr = wordsArr.join(" ");
    // Return the reversed string
    return reversedStr;
  }
  const str = "The quick brown fox";
  const reversed = reverseWords(str);
  console.log("The given string is : "+str); // Output: "fox brown quick The"
  console.log("The reversed string is : "+reversed); // Output: "fox brown quick The"
    