function shiftArrayValues(arr) {
    for(var i = 1; i < arr.length; i++){
        arr[i-1] = arr[i]
    }
    arr[arr.length-1] = 0
    console.log(arr)
}
shiftArrayValues([2,5,7,8,3])
