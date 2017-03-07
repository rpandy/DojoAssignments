// Array: Pop Front
// Given an array, remove and return the value at the beginning of the array.
// Do this without using any built-in array methods except pop().

function popFront(arr) {
var i = 0

// we used a while loop because we are unsure of the array length
    while (arr.length >= 1) {
        if (arr.length === 1) {
            console.log(arr[0])
            break;
        }
        arr.pop()

        console.log(arr)
    }
}
popFront([43,2,3,4,5,6,7]);
