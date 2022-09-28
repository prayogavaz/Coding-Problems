'''You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.'''

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if (len(nums)) == 1:
            return nums[0]
            
        if (len(nums)) == 0:
            return 0
        
        maximumLoot = [0 for _ in range(len(nums))]
        
  
        maximumLoot[0] = nums[0]
        maximumLoot[1] = max(nums[0], nums[1])
        for i in range(2,len(nums)):
            
            maximumLoot[i] = max(maximumLoot[i-1], maximumLoot[i-2]+nums[i])
        
        
        return max(maximumLoot)
