class Solution:
    def isPalindrome(self,s,left,right):
        if left>right or len(s)==0:
            return 0
        while(left>=0 and right<len(s) and s[left]==s[right]):
            left-=1
            right+=1
        return right-left-1
        
    def longestPalindrome(self, s: str) -> str:
        start=0
        end=0
        ans=0
        for i in range(len(s)):
            l1=self.isPalindrome(s,i,i)
            l2=self.isPalindrome(s,i,i+1)
            _max = max(l1,l2)
            if _max>ans:
                ans=_max
                start = i-(_max-1)//2
                end = i+_max//2
        return s[start:end+1]