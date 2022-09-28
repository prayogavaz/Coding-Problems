'''Given an array, rotate the array to the right by k steps, where k is non-negative.'''

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        
        k = k%len(nums)
        self.reverse(nums,0,len(nums)-1)
        self.reverse(nums,0,k-1)
        self.reverse(nums,k,len(nums)-1)
        
        
    def reverse(self, nums, x, y):
        if y<=x:
            return
        for i in range(int((y-x)/2)+1):
            nums[x+i],nums[y-i] = nums[y-i],nums[x+i]
