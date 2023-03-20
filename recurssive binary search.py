def binary_search_recurssive(arr, target, left, right):
    if left <= right:
        mid = (left + right) // 2
        
        
        if target == arr[mid]:
            return mid
        elif target < arr[mid]:
            binary_search_recurssive(arr, target, left, mid - 1)
            
        elif target > arr[mid]:
            binary_search_recurssive(arr, target, mid + 1, right)
    
    return -1


print(binary_search_recurssive([1,2,3,4,5], 1, 0, 5))