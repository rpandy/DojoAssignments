function sumToOneDigit(num) {
    var output = [];
    var sNumber = num.toString(); //turn the number into a string

    for(var i = 0; i < sNumber.length; i++){
        output.push(sNumber.charAt(i));

        console.log(output)
    }
    console.log(output)
}
sumToOneDigit(928);

function addingDigits(arr) {
    arrSum = 0
    for(var i = 0; i < arr.length; i++){
        if(arr[i] < 10)
        arrSum += arr[i]
    }
}
