'''Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.'''

class Solution:
    def searchInsert(self, nums: List[int], target: int, left = 0, right = 'b') -> int:
        
        
        if right == 'b':
            right = len(nums)-1
            
        
        if right == left + 1 or left == right:
            
            if target == nums[right]:
                return right
            if target == nums[left]:
                return left
            if target > nums[right]:
                return right+1
            if target < nums[left]:
                return left
            return left + 1
            
            
        middle = int((left+right)/2)
        
        
        if nums[middle] == target:
            return middle
        
        
        if target < nums[middle]:
            return self.searchInsert(nums,target,left,middle)
        else:
            return self.searchInsert(nums,target,middle,right)
