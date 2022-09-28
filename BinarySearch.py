'''Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.'''

class Solution(object):
    def search(self, nums, target):
        
        
        return self.searchR(nums,target,0,len(nums)-1)
            
        
    def searchR(self, nums, target, left, right):
            
            middle = int((right+left)/2)
        
            if nums[middle] == target:
                return middle

            if right <= left:
                return -1

            if target < nums[middle]:
                return self.searchR(nums,target,left,middle-1)
            else:
                return self.searchR(nums,target,middle+1,right)
