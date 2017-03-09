function minToFront(arr) {
    //create an undefined
    arr[arr.length + 1] = 1
    arr.pop()
    console.log(arr)
    var max = 0
    var min = 0
    for (var i = 0; i < arr.length; i++) {
        if (arr[i] > max) {
            max = arr[i]
        }
        console.log(max)
        arr[arr.length - i] = max
    }
    console.log(arr)
}
minToFront([1,4,3,8,7,5,2])
