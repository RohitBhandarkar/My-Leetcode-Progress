class Solution:
    def jump(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return 0
        if n==2:
            return 1
        ans=0
        l=r=0
        while r<n-1:
            _max =0
            for i in range(l,r+1):
                _max=i+nums[i] if i+nums[i]>_max else _max
            l=r+1
            r=_max
            ans+=1
        return ans