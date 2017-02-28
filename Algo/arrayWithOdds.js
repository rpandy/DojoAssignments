function arrayWithOdds() {
    var arr = []
    for(var i = 0; i <= 255; i++){
        if(i % 2 === 1){
            arr.push(i)
        }
    }
    console.log(arr)
}

arrayWithOdds();
