// Rockin' the Dojo Sweatshirt
// Ever since you arrived at the Dojo, you wanted one of those cool Coding Dojo sweatshirts -
// maybe even more than one. Let's say they cost $20 (including tax), but friendly
// Josh will give a 9% discount if you buy two, or a nice 19% discount if you buy three,
// or a sweet 35% discount if you buy four or more. He only accepts cash and doesn't
// have coins, so you have to round up to the nearest dollar. Build a function sweatshirtPricing(num)
// that, given how many sweatshirts you want, returns the cost.

//input: number of shirts.
//output how much you paid for X amount of sweatshirts

//if statements comparing the amount of shirts with the discount offered for each.
//do we include the tax rate? if so... how much?
function dojoSweatshirt(num) {
    var sweatshirt = 20
    var friendly = .09
    var nice = .19
    var sweet = .35
    var cost = 0

    if(num === 1){
        (cost = sweatshirt);
        console.log(num + " sweatshirt will cost you: " + cost + " dollars!")
    }
    else if(num === 2){
        cost = Math.ceil(num * (sweatshirt*(1-friendly)))
        console.log(num + " sweatshirts will only cost you: " + cost + " dollars!")
    }
    else if(num === 3){
        cost = Math.ceil(num * (sweatshirt*(1-nice)))
        console.log(num + " sweatshirts will only cost you: " + cost + " dollars!")
    }
    else if(num === 4) {
        cost = Math.ceil(num * Math.ceil(sweatshirt*(1-sweet)))
        console.log(num + " sweatshirts will only cost you: " + cost + " dollars!")
    }
    //else console.log("thats way too many shirt")
}

dojoSweatshirt(2);
