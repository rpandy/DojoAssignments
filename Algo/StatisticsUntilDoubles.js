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

    var currentRoll = rollFunction(); // used a call back function for a different roll each time.
    var previousRoll = 0

    while (currentRoll != previousRoll) {
        if (currentRoll != previousRoll) {
            var temp = 0
            temp = currentRoll
            currentRoll = rollFunction()
            var previousRoll = temp
        }
        console.log("the current roll of " + currentRoll + " & the previous roll of " + previousRoll + " are not the same number")
    }
    console.log(currentRoll + " & " + previousRoll + " are finally the same number")

}
statisticsUntilDoubles()
