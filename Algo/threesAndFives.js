// Threes And Fives
// Create ThreesFives() that adds values from 100 and 4000000
//(inclusive) if that value is evenly divisible by 3 or 5 but not both. Display the final sum in the console.

// Second: Create BetterThreesFives(start,end) that allows you to enter arbitrary start and end values for your range. Think of your above ThreesFives() function as BetterThreesFives(100,4000000).

function threesAndFives() {
    var sum = 0
    for(var i = 100; i <= 4000000; i++){
        if(i % 3 === 0 && i % 5 === 0){
            continue;
        }
        else if(i % 3 === 0){
            sum +=i
        }
        else if(i % 5 === 0){
            sum +=i
        }
    }
    console.log(sum)
}
threesAndFives()



function threesAndFivesImproved(alpha, omega) {
    var sum = 0
    for(var i = alpha; i <= omega; i++){
        if(i % 3 === 0 && i % 5 === 0){
            continue;
        }
        else if(i % 3 === 0){
            sum +=i
            console.log(sum);
        }
        else if(i % 5 === 0){
            sum +=i
            console.log(sum);
        }
    }
    console.log(sum)
}
threesAndFivesImproved(1,10)
