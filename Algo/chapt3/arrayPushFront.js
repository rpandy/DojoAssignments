// Array: Push Front
// Given an array and an additional value, insert this value at the beginning of the array.
// Do this without using any built-in array methods.

function arrayPushFront(arr, num) {
var newArr = []

newArr.push(num)
for (var i = 0; i < arr.length; i++) {
    newArr.push(arr[i])
}
console.log(newArr)

}
arrayPushFront([1,2,3,4,5,6], 7)
