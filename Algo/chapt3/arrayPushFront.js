// Array: Push Front
// Given an array and an additional value, insert this value at the beginning of the array.
// Do this without using any built-in array methods.

function arrayPushFront(arr, num) {
    console.log( arr + " before we add " + num + " to index 0")
    arr[0] = (num)
    console.log(arr)
}
arrayPushFront([1,2,3,4,5,6], 7)
