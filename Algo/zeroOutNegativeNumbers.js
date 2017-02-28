function zeroOutNegativeNumbers(arr) {
    for(var i = 0; i < arr.length; i++){
        if(arr[i] < 0){
            arr[i] = 0
        }
    }
    console.log(arr)
}
zeroOutNegativeNumbers([2,5,7,3,-6,4,-67])
