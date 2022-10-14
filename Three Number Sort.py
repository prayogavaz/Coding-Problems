'''Sort an interger array containing 3 numbers, whose order is given in a seperate array'''

def threeNumberSort(array, order):
    

    firstElementBoundary = 0
    lastElementBoundary = len(array)-1

    i = 0
    while i < len(array):

        if array[i] == order[0] and i > firstElementBoundary:
            array[firstElementBoundary], array[i] = array[i], array[firstElementBoundary]
            firstElementBoundary += 1
        elif array[i] == order[2] and i < lastElementBoundary:
            array[lastElementBoundary], array[i] = array[i], array[lastElementBoundary]
            lastElementBoundary -= 1
        else:
            i +=1

    return array
