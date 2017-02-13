// // First Plus Length
// // Given an array, return the sum of the first value in the array, plus the array’s length.
// What happens if the array’s first value is not a number, but a string (like "what?") or a boolean (like false).

function firstPlusLength(num1, num2, num3, num4) {
    var arr = [num1,num2,num3,num4];
    var sum = 0;

    sum = arr[0] + arr.length;
    //return sum
    return console.log(sum);
}

firstPlusLength(10,4,6,4)

// A string in the first digit will simply concat the string with the length of the array: "String4"
// A boolean in the first digit will register as a 0 (false) or 1 (true) and will add that number to the length of the string.
// true: "5"
// false; "4"
