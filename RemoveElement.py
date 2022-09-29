'''Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The relative order of the elements may be changed.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.'''


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        
        i = 0
        j = len(nums)-1
        
        if len(nums) == 1:
            if nums[0] == val:
                return 0
            else:
                return 1
        
        while i < j:
 
            while i < len(nums) -1 and nums[i] != val:
                i += 1
            while j >= 0 and nums[j] == val:
                j -= 1
  
            if j == -1 and nums[0] == val:
                return 0
                
            if  i < j and nums[i] == val and nums[j] != val:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
            
        if j > 0 and j < len(nums) and nums[j] == val:
            return j
        
        return j+1
