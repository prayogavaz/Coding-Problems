'''Given an array representing heights of buildings. The array has buildings from left to right as shown in below diagram, count number of buildings facing the sunset. It is assumed that heights of all buildings are distinct.'''

def sunsetViews(buildings, direction):
    
    result = []
    if direction == 'EAST':

        left = len(buildings)-1
        tallest = -1

        while left >= 0:
            if buildings[left] > tallest:
                result.insert(0,left)
            tallest = max(buildings[left], tallest)
            left -= 1
    else:

        right = 0
        tallest = -1
        while right < len(buildings):
            if buildings[right] > tallest:
                result.append(right)
            tallest = max(buildings[right], tallest)
            right += 1

    return result
        
