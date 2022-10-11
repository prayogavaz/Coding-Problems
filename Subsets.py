'''Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.'''


from copy import deepcopy

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        if len(nums) == 0:
            return [[]]

        if len(nums) == 1:
            return [[], [nums[0]]]


        remainingSubsets = self.subsets(nums[1:])

        remainingSubsetsCopy = deepcopy(remainingSubsets)

        for remainingSubset in remainingSubsets:

            remainingSubsetsCopy.append([nums[0]]+remainingSubset)

        return remainingSubsetsCopy
