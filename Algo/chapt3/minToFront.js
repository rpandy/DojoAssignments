function minToFront(arr) {
    //move the lowest digit to the front
    //move the

    //create a sparce space (arr[arr.length])
    arr[arr.length] = 999
    console.log(arr)
    //find the lowest digit
    var min = 999
        //move all digits up one
    for (var i = 0; i < arr.length; i++) {
            var temp = arr[arr.length]
            arr[arr.length] = arr[arr.length-1]

    }
            console.log(arr)
        }
        console.log(arr)
    }

}
minToFront([4,2,1,3,5])
