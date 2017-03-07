// Statistics Until Doubles
// Here’s another game for our New Year’s Eve party.
// Implement a ’20-sided die’ that randomly returns integers between 1 and 20 inclusive.
// Roll these, tracking statistics until you get a value twice in a row.
// Display number of rolls, min, max, and average.
function rollFunction() {
    roll = Math.floor((Math.random()*20)+1)
    return roll;
}
function statisticsUntilDoubles() {

    var currentRoll = rollFunction();
    var previousRoll = 0

    while (currentRoll != previousRoll) {
        if (currentRoll != previousRoll) {
            var temp = 0
            temp = currentRoll
            currentRoll = rollFunction()
            var previousRoll = temp
        }
        console.log(currentRoll)
        console.log(previousRoll)
        
    }
    console.log("this is the current roll: " + currentRoll)
    console.log("this is the previous roll: " + previousRoll)
}
statisticsUntilDoubles()
