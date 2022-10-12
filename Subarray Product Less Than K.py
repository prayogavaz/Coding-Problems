'''Given an array of integers nums and an integer k, return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than k.'''

'''Constraints:

1 <= nums.length <= 3 * 104
1 <= nums[i] <= 1000
0 <= k <= 106'''

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:

        count = 0

        left = 0
        right = 0

        product = 1

        while right < len(nums):

            product *= nums[right]

            while left < right and product >= k:
                product /= nums[left]
                left += 1

            if product < k:
                count += (right-left) + 1
    
            right += 1

        return count
