function mergeSort(arr) {
    if (arr.length <= 1) {
      return arr;
    }
  
    const middle = Math.floor(arr.length / 2);
    const leftArr = arr.slice(0, middle);
    const rightArr = arr.slice(middle);
  
    return merge(mergeSort(leftArr), mergeSort(rightArr));
  }
  
  function merge(leftArr, rightArr) {
    const sortedArr = [];
    let leftIndex = 0;
    let rightIndex = 0;
  
    while (leftIndex < leftArr.length && rightIndex < rightArr.length) {
      if (leftArr[leftIndex] < rightArr[rightIndex]) {
        sortedArr.push(leftArr[leftIndex]);
        leftIndex++;
      } else {
        sortedArr.push(rightArr[rightIndex]);
        rightIndex++;
      }
    }
  
    return sortedArr.concat(leftArr.slice(leftIndex), rightArr.slice(rightIndex));
  }
  const arr = [7, 3, 9, 4, 1, 8, 2, 6, 5];
  const sortedArr = mergeSort(arr);
  console.log(sortedArr); // Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
    