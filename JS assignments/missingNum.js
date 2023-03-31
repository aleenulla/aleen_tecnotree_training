function findMissingNumber(arr) {
    const n = arr.length + 1;
    const sum = (n * (n + 1)) / 2;
    let arrSum = 0;
    for (let i = 0; i < arr.length; i++) {
      arrSum += arr[i];
    }
    const missingNumber = sum - arrSum;
    return missingNumber;
  }

  const arr = [1, 2, 4, 5, 6];
const missingNumber = findMissingNumber(arr);
console.log("The missing number is : "+missingNumber); // Output: 3
