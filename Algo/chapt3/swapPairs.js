/*Array: Swap Pairs
Swap positions of successive pairs of values of given array.
If the length is odd, do not change the final element.
For [1,2,3,4], return [2,1,4,3]. For example, change input ["Brendan",true,42] to [true,"Brendan",42].
As with all array challenges, do this without using any built-in array methods.*/

function swapPairs(arr) {
for (var i = 0; i < arr.length; i++) {
    if(arr.length % 2 === 0){
        var temp = arr[i]
        arr[i] = arr[i+1]
        arr[i+1] = temp
        i++
            //console.log(arr)
    }
    else if (i === arr.length-1) {
        break;
    }
    else
    {
        var temp = arr[i]
        arr[i] = arr[i+1]
        arr[i+1] = temp
        i++
        //console.log(arr)
        }
    }
    console.log(arr)
}
swapPairs([1,2,3,4,5,6])
