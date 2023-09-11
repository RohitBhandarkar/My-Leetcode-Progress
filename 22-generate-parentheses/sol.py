class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans=[]
        ans = self.backtrack(string='',open=0,close=0,arr=ans,n=n)
        return ans
    
    def backtrack(self,string,open,close,arr,n):
        if open==n and close==n:
            arr.append(string)
            return
        if open<n:
            self.backtrack(string+'(',open+1,close,arr,n)
        if close<n and close<open:
            self.backtrack(string+')',open,close+1,arr,n)
        return arr            