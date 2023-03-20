def search(arr, target):
    
    l = 0
    r = len(arr) - 1
    
    while l <= r:
        mid = (l + r) / 2
        mid = int(mid)
        if target == arr[mid]:
            return mid
        elif target < arr[mid]:
            r = mid-1
            
        else:
            l = mid + 1
            
    return -1

arr = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
target = 17

print(search(arr, target))
