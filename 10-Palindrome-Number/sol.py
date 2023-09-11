class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        y = str(x)
        ans=""
        for i in range(len(y)-1,-1,-1):
            ans+=y[i]
        if ans==y:
            return True
        return False