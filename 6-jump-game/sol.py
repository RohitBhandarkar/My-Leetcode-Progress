class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n=len(nums)
        if n==1:
            return True
        ans=0
        l=r=0
        while r<n-1:
            if l>r:
                return False
            _max =0
            for i in range(l,r+1):
                _max=i+nums[i] if i+nums[i]>_max else _max
            l=r+1
            r=_max
            ans+=1
        return True