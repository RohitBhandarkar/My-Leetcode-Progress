from collections import defaultdict
class Solution:
    def defVal():
        return 1
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n,ans,suf = len(nums),[1]*len(nums),1
        for i in range(1,n):
            ans[i]=ans[i-1]*nums[i-1]
        for i in range(n-1,-1,-1):
            ans[i]*=suf
            suf *= nums[i]
        return ans