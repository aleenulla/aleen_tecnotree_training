function findNthLargest(arr, n) {
    // Sort the array in descending order
    arr.sort((a, b) => b - a);
    // Return the nth largest element
    return arr[n - 1];
  }
  const arr = [5, 3, 1, 4, 2];
  const nthLargest = findNthLargest(arr, 3);
  console.log("Nth largest Nnumber : "+nthLargest); // Output: 3
    