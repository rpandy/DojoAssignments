function greaterThanY(arr, Y) {
    var count = 0
    for(var i = 0; i < arr.length; i++){
        if(arr[i] > Y){
            console.log(arr[i]);
            count++
        }
    }
    console.log("there are " + count + " figures greater than Y in the array")
}

greaterThanY([3,4,2,6,7,8,9], 5)
