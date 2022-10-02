'''There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).

Before being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become [4,5,6,6,7,0,1,2,4,4].

Given the array nums after the rotation and an integer target, return true if target is in nums, or false if it is not in nums.

You must decrease the overall operation steps as much as possible.'''


class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left = 0
        right = len(nums)-1
        middle = int((left+right)/2)

        pivotIndex = self.getPivotIndexR(nums,left,right)

        if pivotIndex == -1:
            return self.binarySearchR(nums,target,left,right)

        if nums[middle] == target:
            return middle

        if target > nums[middle]:
            if pivotIndex > middle:
                return self.binarySearchR(nums,target,middle,pivotIndex-1)
            elif pivotIndex <= middle:
                a = self.binarySearchR(nums,target,left,pivotIndex-1)
                if a == -1:
                    return self.binarySearchR(nums,target,middle,right)
                else:
                    return a

        if target < nums[middle]:
            if pivotIndex < middle:
                return self.binarySearchR(nums,target,pivotIndex, middle)
            elif pivotIndex > middle:
                a = self.binarySearchR(nums,target,left,middle)
                if a == -1:
                    return self.binarySearchR(nums,target,pivotIndex,right)
                else:
                    return a
            else:
                return -1


    def getPivotIndexR(self, nums, left = 0, right = -1):

        if left == right or len(nums) == 0:
            return -1

        if right == -1:
            right = len(nums)-1

        if left+1 == right:
            if nums[left] > nums[right]:
                return right
            else:
                return -1

        middle = int((left+right)/2)

        if nums[middle] < nums[middle-1]:
            return middle

        if nums[middle] > nums[right]:
            return self.getPivotIndexR(nums,middle,right)
        else:
            return self.getPivotIndexR(nums,left,middle)
        


    def binarySearchR(self, nums, target, left = 0, right = -1):

        if len(nums) == 0:
            return -1

        if right == -1:
            right = len(nums)-1

        if left == right:
            if nums[left] == target:
                return left
            else:
                return -1

        middle = int((left+right)/2)

        if left+1 == right:
            if nums[left] == target:
                return left
            elif nums[right] == target:
                return right
            else:
                return -1

        if nums[middle] == target:
            return middle

        if target < nums[middle]:
            return self.binarySearchR(nums,target,left,middle)
        else:
            return self.binarySearchR(nums,target,middle,right)
