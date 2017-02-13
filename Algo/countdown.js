//Countdown
/*Create a function that accepts a number as an input.
Return a new array that counts down by one, from the number (as array’s ‘zero’th element) down to 0 (as the last element).
How long is this array?*/

function countdown(num) {
    var arr = []
    var count = num

    for(var i = 0; i <= num; i++){
        arr[i] = count;
        count--

    }
    return arr;
}
console.log(countdown(14));

//The array will always be one digit longer than var num.
