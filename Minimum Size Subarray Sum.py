'''Given an array of positive integers nums and a positive integer target, return the minimal length of a contiguous subarray [numsl, numsl+1, ..., numsr-1, numsr] of which the sum is greater than or equal to target. If there is no such subarray, return 0 instead.'''

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        left = 0
        right = 0

        total = 0
        minlength = float('inf')
        while right < len(nums):

            total += nums[right]

            while left <= right and total >= target:
                minlength = min(minlength, right-left+1)
                total -= nums[left]
                left += 1

            right += 1

        if minlength == float('inf'):
            return 0

        return minlength
