## Problem: Letter Combinations of a Phone Number

# Statement:

<p>
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

</p>

- Date: 13th September 2023
- Difficulty: Medium
- Solved: Yes
- Problem type: String,Dict, code optimization
- Language used: Python

### Initial thoughts / approaches

- make a dictionary of all the numbers and their corresponding letters
- have to find all possible combinations of length len(digits) without repeating letters
- can use python's combination module but there should be a better way
- since digits wont be more than 4, O(n!) should be fine
- can be done by calling another function
- Optimized by reducing from O(n!) to O(n^3)
- damn..worked fantastic the first time

### My solution

```
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits)==0:
            return []
        phone={'2':['a','b','c'],'3':['d','e','f'],'4':['g','h','i'],'5':['j','k','l'],'6':['m','n','o'],'7':['p','q','r','s',],'8':['t','u','v'],'9':['w','x','y','z']}

        if len(digits)==1:
            return phone[digits]
        ans=phone[digits[0]]
        for i in range(1,len(digits)):
            ans = self.combine(ans,phone[digits[i]])

        return ans

    def combine(self,l1,l2):
        ans=[]
        for i in range(len(l1)):
            for j in range(len(l2)):
                ans.append(l1[i]+l2[j])
        return ans
```

### Result

<img src="../images/problem17.jpg">
