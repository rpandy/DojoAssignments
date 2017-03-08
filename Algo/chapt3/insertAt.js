/*Array: Insert At
Given an array, index, and additional value, insert the value into the array at given index.
Do this without using built-in array methods.
You can think of PushFront(arr,val) as equivalent to InsertAt(arr,0,val).*/

function insertAt(arr,idx,num) {
var newArr = []
    for(var i = 0; i < arr.length; i++){
        if(idx === i){
            //we use the index and the iteration to determine whether or not to push the new num (999)
            newArr.push(num)
        }
        //if the idx and i != then we can push the old value into newArr.
        else newArr.push(arr[i])
    }
    console.log(newArr)
}

insertAt([1,2,3,4,5,6],3,999);
