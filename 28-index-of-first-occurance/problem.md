## Problem: Find the Index of the First Occurrence in a String

# Statement:

<p>
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
</p>

- Date: 20th August 2023
- Difficulty: Easy
- Solved: Yes
- Problem type: String functions
- Language used: Python

### My solution

```
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)
```

### Result

<img src="../images/problem28.jpg">
