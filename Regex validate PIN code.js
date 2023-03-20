function validatePIN (pin) {
    //return true or false
    if (!(pin.length===4 || pin.length===6)){
      return false;
    }
    
    var i;
    for ( i = 0; i < pin.length; i++ ) {
        let bool = isNaN(pin[i])
        if (bool){
            return false;
        }
    }
    return true;
}



console.log(validatePIN('123'))