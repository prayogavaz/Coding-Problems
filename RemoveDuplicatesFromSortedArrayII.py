'''Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.'''


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        if len(nums) == 0 or len(nums) == 1 or len(nums) == 2:
            return len(nums)

        position=2
        i = 2

        if nums[i] == nums[i-1] and nums[i-1] != nums[i-2]:
            position = 3
            i = 3

        while i < len(nums):

            if nums[i]!=nums[i-1]:
                nums[position]=nums[i]
                position += 1
                i += 1
                if i < len(nums) and nums[i] == nums[i-1]:
                    nums[position]=nums[i]
                    position += 1
                    i += 1
            else:
                i += 1

        return position
