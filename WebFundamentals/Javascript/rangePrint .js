// function rangePrint(first, last, skip) {
//     while(first < last){
//         console.log(first)
//         first+=skip
//     }
//
// }
// rangePrint(-1,-29,2)

// function rangePrint(first, last, skip) {
//     while(first < last){
//         console.log(first)
//         first+=skip
//     }
//
// }
// rangePrint(-29,29,2)

//if skip parameter is undefined
function rangePrint(first, last, skip) {
    if(typeof(skip) === 'undefined'){
        skip = 1;
    }
        while(first < last){
            console.log(first);
            first+=skip
    }
    while(first < last){
        console.log(first);
        first+=skip
    }
}
rangePrint(2,29)

//?? if last and skip are undefined.
// function rangePrint(first, last, skip) {
//     if(typeof(skip & last) === 'undefined'){
//
//         last = first;
//         first = 0;
//         skip = 1;
//     }
//         while(first < last){
//             console.log(first);
//             first+=skip
//     }
//     while(first < last){
//         console.log(first);
//         first+=skip
//     }
// }
// rangePrint(8)
