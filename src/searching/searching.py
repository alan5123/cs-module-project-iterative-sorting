def linear_search(arr, target):
    # Your code here
    for i in range(0, len(arr)):
        if arr[i] == target:
            return i

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    #first we need to set the low and high
    low = 0
    high = len(arr) - 1 

# if the low is lower than the high or equal to it run this function
    while low <= high:
    
    # Find the middle by adding the high and low and dividing and flooring it
        mid = (high + low) // 2

    #if the targeted number is equal to middle point return 
        if target == arr[mid]:
            return mid

# if the target is less than the middle point we can eliminate the right side of the arr we do that by setting the high one down below the mid
        if target < arr[mid]:

            high = mid - 1


# if the target is grater than the middle point we cam elimate left side of the arr by setting the new low to mid plus one
        if target > arr[mid]:
        
            low = mid + 1


    return -1  # not found
