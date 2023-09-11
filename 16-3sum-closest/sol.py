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
