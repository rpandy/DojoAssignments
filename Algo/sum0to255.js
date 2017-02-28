function IntsSum() {
    var sum = 0
    for(var i = 0; i <= 255; i++){
        sum+=i
        console.log("the current integer is: " + i)
        console.log("The running sum is: " + sum);
    }
}

IntsSum()
