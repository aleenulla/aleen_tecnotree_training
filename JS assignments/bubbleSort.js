function bubbleSort(arr) {
    const n = arr.length;
    for (let i = 0; i < n - 1; i++) {
      for (let j = 0; j < n - i - 1; j++) {
        if (arr[j] > arr[j + 1]) {
          // Swap arr[j] and arr[j+1]
          const temp = arr[j];
          arr[j] = arr[j + 1];
          arr[j + 1] = temp;
        }
      }
    }
    return arr;
  }

const arr = [3, 2, 1, 5, 4];

console.log("-------------------------------Bubble Sort------------------------------------") ; // Output: [1, 2, 3, 4, 5]
console.log("The give array is : "+arr); 
const sorted = bubbleSort(arr);
console.log("The sorted array is : "+sorted);
console.log("------------------------------------------------------------------------------");
