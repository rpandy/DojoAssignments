/*Array: Remove At
Given an array and an index into array, remove and return the array value at that index.
Do this without using built-in array methods except for the pop().
Think of PopFront(arr) as equivalent to RemoveAt(arr,0).*/

function removeAt(arr, idx) {
var newArr = []
    for(var i = 0; i < arr.length; i++){
        if(i === idx){
            //if the index and the iteration are equal then we know the number to exclude from new arr.
            continue;
        }
        //if the idx and i != then we can push the old value into newArr.
        else newArr.push(arr[i])
    }
    console.log(newArr)
}

removeAt([1,2,3,4,5,6,7],3)
