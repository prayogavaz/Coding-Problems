'''Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.'''

class Solution:
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        existence = {}
        
        for i,num in enumerate(nums):
            
            if num not in existence.keys():
                
                existence[num] = [i]
                
            else:
                
                existence[num].append(i)
                
                
            if target-num in existence.keys():
                
                remnantIndex = existence[target-num][0]
                
                if i != remnantIndex:
                    
                    return [i,remnantIndex]
            
        
        for i, num in enumerate(nums):
            
            if target-num in existence.keys():
                
                remnantIndex = existence[target-num][0]
                
                if i != remnantIndex:
                    
                    return [i,remnantIndex]
