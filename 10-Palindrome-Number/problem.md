## Problem: Palindrome Number

# Statement:

<p>
Given an integer x, return true if x is a 
palindrome, and false otherwise.
</p>

- Date: 4th October 2022
- Difficulty: East
- Solved: Yes
- Problem type: String Type
- Language used: Python

### My solution

```
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        y = str(x)
        ans=""
        for i in range(len(y)-1,-1,-1):
            ans+=y[i]
        if ans==y:
            return True
        return False
```

### Result

<img src="../images/problem10.jpg">
