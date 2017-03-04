function fibonacci(num) {
    var fibArr = [0,1]
    var fibSum = 0

    for(var i = 1; i < num; i++){
        fibSum = fibArr[i] + fibArr[i-1]
        fibArr.push(fibSum)
        console.log(fibArr)
    }
    console.log(fibSum);
}

fibonacci(15);
