'''Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.'''

from copy import deepcopy

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        if len(nums) == 1:
            
            return [[nums[0]]]
       
        
        remainingPermutations = self.permute(nums[1:])
        
        remainingPermutationsCopy = deepcopy(remainingPermutations)
        
        for permutation in remainingPermutationsCopy:
            
            remainingPermutations.remove(permutation)
       
            for i in range(len(permutation)+1):
                
                permutationCopy = deepcopy(permutation)
                permutationCopy.insert(i,nums[0])
                remainingPermutations.append(permutationCopy)
            
            
        return remainingPermutations
        
