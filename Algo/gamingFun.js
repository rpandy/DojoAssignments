
//Create function rollOne() to return a randomly selected integer between 1 and 6 (inclusive).
//we declare roll outside of any functions to give it global scope.
//math.random will give you a random number between 0 and  close to 1. To get a specific number we multiply that argument by the number we want
//and then add the number we wish to start with as an offset.
//the math.floor argument drops the decimal places and row
roll = Math.floor((Math.random() * 6 ) + 1);

function rollOne() {
    return Math.floor((Math.random() * 6 ) + 1);
}

rollOne();

// Second, create a function playFives(num), which should call rollOne() multiple times – 'num'
// times, in fact, where 'num' is input parameter to playFives(num).
// Each time, it should print the value rollOne() returns, and if that return value is 5, also print “That’s good luck!”

function playFives(num){
var diceRoll = rollOne();

for(var i = 0; i < num; i++){
    //function rollOne can be invoked here because it has a global scope.
    if(rollOne() === 5){
        console.log("that's good luck!")
    }
    else console.log("unlucky")
}
}
playFives(5)

// Third, create a new function named playStatistics(), which should call rollOne() eight times
// (but not print anything after each call). After the last of these eight calls,
// it should print out the lowest and highest values that it received from rollOne, among those eight calls.

function playStatistics() {
var max = 0
var min = 7 // min cannot be set at 0 because there will never be a rollOne below 0
    for(var i = 0; i < 8; i++){
        //we will need a roll temp variable because each rollOne is a new roll
        var roll = rollOne();
        if(roll > max){
            max = roll;
        }
        if(roll < min){
            min = roll;
        }
    }
console.log("your max and min values are " + max + " & " + min + "  respectively...")
}
playStatistics()

// Fourth, make a copy of playStatistics and add code to make playStatistics2(),
// so that at the end (in addition to printing high/low rolls), it also prints the total sum of all eight rolls.

function playStatistics2() {
var max = 1
var min = 6
var sum = 0 //add a sum variable to keep track of the sum as we iterate through the rolls

    for(var i = 0; i < 8; i++){
        var roll = rollOne()
        if(roll > max){
            max = roll;
        }
        if(roll < min){
            min = roll;
        }
        sum+=roll
    }
console.log("The sum of all 8 rolls is " + sum)
}
playStatistics2()

function playStatistics3(num) {
var max = 1
var min = 6
var sum = 0

    for(var i = 0; i < num; i++){
        var roll = rollOne()
        if(roll > max){
            max = roll;
        }
        if(roll < min){
            min = roll;
        }
        sum+=roll
    }
console.log("The sum of all " + num + " rolls is " + sum)
}
playStatistics3(54)

function playStatistics4(num) {
var max = 1
var min = 6
var sum = 0

    for(var i = 0; i < num; i++){
        var roll = rollOne()
        if(roll > max){
            max = roll;
        }
        if(roll < min){
            min = roll;
        }
        sum+=roll
    }
    var avg = sum / num

console.log("The average of all " + num + " rolls is " + avg)
}
playStatistics4(54)
