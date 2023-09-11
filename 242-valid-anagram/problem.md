## Problem: Valid Anagram

# Statement:

<p>
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

</p>

- Date: 11th September 2023
- Difficulty: Easy
- Solved: Yes
- Problem type: String
- Language used: Python

### My solution

```
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
```

### Result

<img src="../images/problem242.jpg">
