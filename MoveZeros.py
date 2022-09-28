'''Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.'''

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        
        
        i = 0
        j = -1
        
        while i < len(nums):
            
            if nums[i] != 0:
                i += 1
                continue
             
            if j == -1:
                j = i+1
            
            while j < len(nums) and nums[j] == 0:
                j += 1
                continue
             
            if j < len(nums):
                nums[i] , nums[j] = nums[j] , nums[i]
            elif j == len(nums):
                break
                
            i += 1
