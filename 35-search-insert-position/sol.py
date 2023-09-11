class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if(len(nums)==1):
            if(nums[0]>=target):
                return 0
            return 1
        mid = int(len(nums)/2)
        if(nums[mid]>target):
            return self.searchInsert(nums[:mid],target)
        elif (nums[mid]<target):
            return mid + self.searchInsert(nums[mid:],target)
        else:
            return mid