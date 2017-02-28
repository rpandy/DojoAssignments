function minManAverage(arr) {
    var min = arr[0]
    var max = arr[0]
    var sum = arr[0]
    for(var i = 0; i < arr.length; i++){
        if(arr[i] > max){
            max = arr[i]
        }
        if(arr[i] < min){
            min = arr[i]
        }
        sum+=arr[i]
    }
    var avg = sum/arr.length
    var newArr = [max, min, avg]

console.log(newArr)
}
minManAverage([2,435,34,65,12,5358,8,5])
