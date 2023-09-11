## Problem: Contains Duplicate

# Statement:

<p>
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
</p>

- Date: 30th January 2023
- Difficulty: Easy
- Solved: Yes
- Problem type: String
- Language used: C++

### My solution

```
#include <set>
class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        set <int> ans;
        for(int i:nums){
            ans.insert(i);
        }
        if(ans.size()==nums.size())return false;
        return true;
    }
};
```

### Result

<img src="../images/problem217.jpg">
