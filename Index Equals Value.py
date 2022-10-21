'''Given an array of n distinct integers sorted in ascending order, write a function that returns the minimum Fixed Point in the array, if there is any Fixed Point present in array, else returns -1. Fixed Point in an array is an index i such that arr[i] is equal to i'''

def indexEqualsValue(array):
    

    left = 0
    right = len(array)-1

    while left <= right:

        if left == right or left + 1 == right:
            if array[left] == left:
                return left
            if array[right] == right:
                return right
            return -1

        middle = int((left+right)/2)

        if middle > array[middle]:
            left = middle
        elif middle <= array[middle]:
            right = middle

    return -1
