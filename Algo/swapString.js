function swapString(arr) {
    for(var i = 0; i < arr.length; i++){
        if(arr[i] < 0){
            arr[i] = 'dojo';
        }
    }
    console.log(arr)
}

swapString([2,4,7,8,9,-2,-3,3])
