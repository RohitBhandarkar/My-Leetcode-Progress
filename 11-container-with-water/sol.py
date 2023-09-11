class Solution:
    def maxArea(self, height: List[int]) -> int:
        i=0
        j=len(height)-1
        cap=0
        while(i<j):
            if height[i]<height[j]:
                area=height[i]*abs(j-i)
                cap = area if area>cap else cap
                i+=1
            else:
                area=height[j]*abs(j-i)
                cap = area if area>cap else cap
                j-=1
        return cap