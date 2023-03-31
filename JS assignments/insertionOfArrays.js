function intersection(arr1, arr2) {
  const result = [];
  for (let i = 0; i < arr1.length; i++) {
    if (arr2.includes(arr1[i])) {
      result.push(arr1[i]);
    }
  }
  return result;
}





const arr1 = [1, 2, 3, 4, 5];
const arr2 = [3, 4, 5, 6, 7];
const result = intersection(arr1, arr2);
console.log(result); // Output: [3, 4, 5]
