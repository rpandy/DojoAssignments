function fancyArray(arr,symbol) {
    fancyOutput = 0
    for(var i = 0; i < arr.length; i++){
        console.log(fancyOutput+symbol+arr[i])
        fancyOutput++
    }
}
fancyArray(["James","Jill","Jane","Jack"],":")

//???
// function fancyArray(arr,symbol,reversed) {
//     if(typeof(reversed) !== 'true'){
//     fancyOutput = arr.length-1
//         for(var i = arr.length-1; i < arr.length; i--){
//             console.log(fancyOutput+symbol+arr[arr.length-1])
//             fancyOutput--
//         }
//
//     }
//     fancyOutput = 0
//         for(var i = 0; i < arr.length; i++){
//             console.log(fancyOutput+symbol+arr[i])
//             fancyOutput++
//         }
// }
// fancyArray(["James","Jill","Jane","Jack"],":",'true')
