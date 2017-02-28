function findAndPrintMax(arr) {
    var max = 0;
    for(var i = 0; i < arr.length; i++){
        if(max < arr[i]){
            max = arr[i];
        }
    }
    console.log("the largest figure in the array is: " + max)
}

findAndPrintMax([24,3,4,5,6,7,8,9])
