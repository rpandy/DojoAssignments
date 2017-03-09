function removeDuplicates(arr) {
    var newArr = []
    for (var i = 0; i < arr.length; i++) {
        if (arr[i] === arr[i-1]) {
            continue;
        }
        else newArr.push(arr[i])
    }
    console.log(newArr)
}
removeDuplicates([1,2,3,3,3,3,3,4,4,5,6,7,7,8])
