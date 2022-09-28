'''Given a string s, you can transform every letter individually to be lowercase or uppercase to create another string.

Return a list of all possible strings we could create. Return the output in any order.'''

from copy import deepcopy

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        
        if len(s) == 1:
            
            if s[0].isalpha():
                return [s[0].lower(),s[0].upper()]
            else:
                return[s[0]]
        
        
        remainingPermutations = self.letterCasePermutation(s[1:])
        
        remainingPermutationsCopy = deepcopy(remainingPermutations)
        
        for permutation in remainingPermutationsCopy:
            
            remainingPermutations.remove(permutation)
            if s[0].isalpha():
                remainingPermutations.append(s[0].lower()+permutation)
                remainingPermutations.append(s[0].upper()+permutation)
            else:
                remainingPermutations.append(s[0]+permutation)
                
        return remainingPermutations
