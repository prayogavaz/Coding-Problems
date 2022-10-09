'''A peak element is an element that is strictly greater than its neighbors.

Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.

You must write an algorithm that runs in O(log n) time.'''

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1


        while left <= right:

            if left == right or left + 1 == right:
                if nums[left] > nums[right]:
                    return left
                else:
                    return right

            middle = int((left+right)/2)

            if nums[middle] > nums[middle-1] and nums[middle] > nums[middle+1]:
                return middle

            if nums[middle] < nums[middle-1]:
                right = middle
            elif nums[middle] < nums[middle+1]:
                left = middle
