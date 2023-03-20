def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    reverse = ''
    x=str(x)
    for i in range (len(x)-1,-1,-1):
        reverse+=x[i]
    print (reverse)
    return reverse == x
