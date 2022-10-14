'''You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:

0 <= j <= nums[i] and
i + j < n
Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].'''


class Solution:
    def jump(self, nums: List[int]) -> int:
        
        reachableIn = [float('inf') for _ in range(len(nums))]

        reachableIn[0] = 0

        for i in range(len(nums)):
            for j in range(i-1,-1,-1):
                if nums[j] + j >= i:
                    reachableIn[i] = min(reachableIn[i], reachableIn[j]+1)

        return reachableIn[len(nums)-1]
      
 
class Solution:
    def jump(self, nums: List[int]) -> int:
        
        left = 0 
        right = 0
        jumps = 0

        while right < len(nums)-1:

            maxReach = 0
            for i in range(left,right+1):
                maxReach = max(maxReach, nums[i]+i)

            left = right+1
            right = maxReach
            jumps += 1

        return jumps
