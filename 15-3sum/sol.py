class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans=[]
        done=[]
        for i in range(len(nums)-1):
            done.append(nums[i])
            req=-nums[i]
            j=i+1
            k=len(nums)-1
            while j<k:
                if nums[j]+nums[k]==req and [nums[i],nums[j],nums[k]] not in ans:
                    ans.append([nums[i],nums[j],nums[k]])
                    j+=1
                    k-=1
                elif nums[j]+nums[k]>req:
                    k-=1
                else:
                    j+=1
        return ans