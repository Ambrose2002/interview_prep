function highAndLow(numbers){
    // ...
    var i;
    var j;
    let arr = []
    number = numbers.split(" ")
    console.log(number)
    for ( i = 0; i < number.length; i++){
      let num = Number(number[i])
      arr.push(num)
      arr.sort((a,b) => a-b)
      
    }
    console.log(arr)
    var x = arr[arr.length-1]
    var y = arr[0]
    return x + ' ' + y;

  }

console.log(highAndLow("8 3 -5 42 -1 0 0 -9 4 7 4 -4"))