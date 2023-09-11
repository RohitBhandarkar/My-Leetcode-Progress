class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        if n==1:
            return nums[0]
        
        mid = int(n/2)
        return max(
            self.maxSubArray(nums[:mid+1]),
            self.maxSubArray(nums[mid+1:]),
            self.crossSum(nums,mid)
        )

    def crossSum(nums,mid):
        #left sum
        max_left_sum=nums[mid]
        for i in range(mid-1,-1,-1):
            if max_left_sum+nums[i]<max_left_sum:
                break
            max_left_sum+=nums[i]

        max_right_sum=nums[mid+1]
        for i in range(mid+2,len(nums)):
            if max_right_sum+nums[i]<max_right_sum:
                break
            max_right_sum+=nums[i]

        return max(max_right_sum,max_left_sum,max_right_sum+max_left_sum)
