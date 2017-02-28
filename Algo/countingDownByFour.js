//Countdown By Fours
//Log positive numbers starting at 2016, counting down by fours (exclude 0), without a FOR loop.

function countingDownByFour() {
var i = 2016

while(i > 1){
    if (i % 4 === 0) {
        console.log(i);
        i--
    }
    else{
        i--
    }
}

}
countingDownByFour();
