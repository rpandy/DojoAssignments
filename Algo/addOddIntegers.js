//Whoa, That Sucker’s Huge…
//Add odd integers from -300,000 to 300,000, and console.log the final sum. Is there a shortcut?
function addOddIntegers() {
var sum = 0
    for(var i = -300000; i<=300000; i++){
        if(i % 2 !== 0){
            sum+=i
        }
    }
    console.log(sum);
}

addOddIntegers();
