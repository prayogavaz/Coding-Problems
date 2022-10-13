'''You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

'''

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        
        if (len(nums)) == 0:
            return 0

        if (len(nums)) <= 2:
            return max(nums)
        
        maximumLootWL = [0 for _ in range(len(nums))]
        maximumLootWF = [0 for _ in range(len(nums))]
        
        maximumLootWL[1] = nums[1]
        maximumLootWL[2] = max(nums[1],nums[2])
        for i in range(3,len(nums)):
            
            maximumLootWL[i] = max(maximumLootWL[i-1], maximumLootWL[i-2]+nums[i])
   
        maximumLootWF[0] = nums[0]
        maximumLootWF[1] = max(nums[0],nums[1])
        for i in range(2,len(nums)-1):
            
            maximumLootWF[i] = max(maximumLootWF[i-1], maximumLootWF[i-2]+nums[i])
       
        return max(max(maximumLootWL),max(maximumLootWF))
