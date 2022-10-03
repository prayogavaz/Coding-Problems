'''Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.'''

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:


        left = 0
        right = len(nums)-1
        firstIndex = -1

        while left <= right:

            print(left,right)
            if left == right or left+1 == right:
                if nums[left] == target:
                    if firstIndex == -1 or firstIndex >= left:
                        firstIndex = left
                elif nums[right] == target:
                    if firstIndex == -1 or firstIndex >= right:
                        firstIndex = right

            middle = int((left+right)/2)

            if nums[middle] == target:
                if firstIndex == -1 or firstIndex >= middle:
                    firstIndex = middle
                    right = middle-1
            elif nums[middle] > target:
                right = middle-1
            else:
                left = middle + 1

        left = 0
        right = len(nums)-1
        secondIndex = -1

        while left <= right:

            if left == right or left+1 == right:
                if nums[left] == target:
                    if secondIndex == -1 or secondIndex <= left:
                        secondIndex = left
                elif nums[right] == target:
                    if secondIndex == -1 or secondIndex <= right:
                        secondIndex = right

            middle = int((left+right)/2)

            if nums[middle] == target:
                if secondIndex == -1 or secondIndex <= middle:
                    secondIndex = middle
                    left = middle+1
            elif nums[middle] > target:
                right = middle-1
            else:
                left = middle + 1

        return [firstIndex, secondIndex]
