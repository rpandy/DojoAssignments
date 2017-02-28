function getAndPrintAverage(arr) {
    var sum = 0
    for(var i = 0; i < arr.length; i++){
        sum+=arr[i];
    }
    var avg = sum/arr.length;
    console.log("the average of the array indices is: " + avg)
}
getAndPrintAverage([23,23,64,8,97,45,23]);
