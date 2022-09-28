'''You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.'''

class Solution(object):
    
    def maxArea(self, height):
        
        maximumCapacity = float('-inf')
        
        leftPointer = 0
        rightPointer = len(height) - 1
        

        while leftPointer < rightPointer:
            
            currentCapacity = (rightPointer-leftPointer) * min(height[rightPointer],height[leftPointer])
            
            maximumCapacity = max(maximumCapacity,currentCapacity)
            
            if height[leftPointer] <= height[rightPointer]:
                leftPointer += 1
            else:
                rightPointer -=1
        
        return maximumCapacity
        
    
    def maxArea2(self, height):
        
        
        maximumCapacity = float('-inf')
        for i in range(len(height)):
                                
            for j in range(i, len(height)):
              
                maximumCapacity = max(min(height[i], height[j]) * (j-i), maximumCapacity)
                                
        return maximumCapacity
