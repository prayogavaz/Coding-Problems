'''Given an unsorted integer array nums, return the smallest missing positive integer.

You must implement an algorithm that runs in O(n) time and uses constant extra space.'''

class Solution:
    
    
     def firstMissingPositive(self, nums: List[int]) -> int:
        
        nums = list(filter(lambda x: x > 0, nums))
        
        if len(nums) == 0:
            return 1
        
        checkPresense = {}
        
        for i in range(len(nums)):
            checkPresense[nums[i]] = 1
            
            
        for i in range(1,max(nums)):
            if i not in checkPresense.keys():
                return i
            
        return max(nums)+1
    
     def firstMissingPositive2(self, nums: List[int]) -> int:
        
        nums = list(filter(lambda x: x > 0, nums))
        
        if len(nums) == 0:
            return 1
        
        new_nums = [0 for _ in range(max(nums)+1)]
        

        for i in range(len(nums)):
            new_nums[nums[i]] = 1
            
        for i in range(1,max(nums)+1):
            if not new_nums[i]:
                return i

        return max(nums)+1
    
     def firstMissingPositive3(self, nums: List[int]) -> int:
        
        nums = list(filter(lambda x: x > 0, nums))
        
        nums.sort()

        if len(nums) == 0 or nums[0] != 1:
            return 1
        
        for i in range(len(nums)-1):
            
            if nums[i] == nums[i+1]:
                
                continue
                
            
            if nums[i+1] != nums[i] + 1:
                
                return nums[i] + 1
                
        return nums[len(nums)-1] + 1
