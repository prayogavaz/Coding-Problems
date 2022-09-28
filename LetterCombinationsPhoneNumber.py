'''Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.'''

from itertools import product
from copy import deepcopy

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        if digits == "":
            return []
        
        dict = {}
        dict['2'] = ['a','b','c']
        dict['3'] = ['d','e','f']
        dict['4'] = ['g','h','i']
        dict['5'] = ['j','k','l']
        dict['6'] = ['m','n','o']
        dict['7'] = ['p','q','r','s']
        dict['8'] = ['t','u','v']
        dict['9'] = ['w','x','y','z']
        
        lists = []
        
        for digit in digits:
            if digit in dict.keys():
                lists.append(dict[digit])
                
 
        result = self.list_product(lists)#[p for p in itertools.product(*lists)]
        return list(map(lambda x: ''.join(x),result))
    
    
    
    def list_product(self,lists):
        
        if len(lists) == 1:
            
            return list(map(lambda x: [x], lists[0]))
        
        
        remainingListsProduct = self.list_product(lists[1:])
        
        remainingListsProductCopy = deepcopy(remainingListsProduct)

        for permutation in remainingListsProductCopy:
            remainingListsProduct.remove(permutation)
            for element in lists[0]:
                remainingListsProduct.append([element] + permutation)
                    
        return remainingListsProduct
            
            
