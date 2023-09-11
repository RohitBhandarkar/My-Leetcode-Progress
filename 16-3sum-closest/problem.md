## Problem: 3Sum Closest

# Statement:

<p>
Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

</p>

- Date: 29th August 2023
- Difficulty: Medium
- Solved: Yes
- Problem type:
- Language used:

### My solution

```
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if len(nums)<=3:
            return sum(nums)
        nums.sort()
        min_diff=99999999999999999999999999
        ans=0
        for i in range(len(nums)-1):
            j=i+1
            k=len(nums)-1
            while j<k:
                curr=nums[i]+nums[j]+nums[k]
                if abs(target-curr)<min_diff:
                    ans=curr
                    min_diff=abs(target-curr)
                if curr>target:
                    k-=1
                else:
                    j+=1
        return ans

```

### Result

<img src="../images/problem16.jpg">
