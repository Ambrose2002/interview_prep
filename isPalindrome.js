var isPalindrome = function(x) {
    x = String(x);
    var reverse = ''
    for (var i=x.length-1; i>=0; i--){
        reverse += x[i];
    }
    console.log(reverse)
    if (reverse === x){
        return true;
    }
    else{
        return false
    }
    
};
