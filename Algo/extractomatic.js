// Extract-o-matic
// Create the extractDigit(num,digitNum) function that given a number and a digit number, returns the numeral value of that digit.
// 0 represents the ones digit, 1 represents the tens digit, etc.
// Given (1824,2), return 8. Given (1824,0), return 4. Given (1824,7), return 0.
//
// Second: handle negative digitNum values, where -1 represents tenths digit (0.x), -2 represents hundredths digit (0.0x), etc.
// Given (123.45,-1), return 4.
//
// Third: handle negative num values as well, doing what you think is appropriate.


// COMPLETE
function extractomatic(num,digitNum) {
//add X amount of 0s to the a 1 for the denominator
var numLength = num.toString().length
var denominator = 1

    for(var i = 0; i <= numLength; i++){
        //test to see if the number you're looking for is even available. If not then log 0. ex. digitNum = 7 would not exist in 1824.
        if(digitNum > numLength){
            console.log(0)
            break;
        }
        //if number of digits declared equals index. we divide the number by the denominator variable and modulo by 10.
        //each iteration changes the denominator by a power of 10. 1 > 10 > 100 > 1000
        else if(digitNum === i){
            console.log(Math.floor(num / denominator) % 10);
            console.log(denominator)
        }
        denominator*=10
    }
}
extractomatic(1824,4)



//function extractomatic(num,digitNum) {
// add X amount of 0s to the a 1 for the denominator
// var numLength = num.toString().length
// var denominator = 1
//
//     for(var i = 0; i <= numLength; i++){
//         if(digitNum > numLength){
//             console.log(0)
//             break;
//         }
//         else if(digitNum === i){
//             console.log(Math.floor(num / denominator) % 10);
//         }
//         else if(digitNum < 0){
//             console.log(Math.floor(num / denominator) % 10);
//         }
//         denominator*=10
//     }
// }
// extractomatic(1824,0)
// console.log(Math.floor(123.45 / .1) % 10); //tenths digit
// console.log(Math.floor(123.45 / .01) % 10); //hundredths digit
