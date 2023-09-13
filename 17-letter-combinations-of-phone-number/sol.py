class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits)==0:
            return []
        phone={'2':['a','b','c'],'3':['d','e','f'],'4':['g','h','i'],'5':['j','k','l'],'6':['m','n','o'],'7':['p','q','r','s',],'8':['t','u','v'],'9':['w','x','y','z']}

        if len(digits)==1:
            return phone[digits]
        ans=phone[digits[0]]
        for i in range(1,len(digits)):
            ans = self.combine(ans,phone[digits[i]])
        
        return ans
    
    def combine(self,l1,l2):
        ans=[]
        for i in range(len(l1)):
            for j in range(len(l2)):
                ans.append(l1[i]+l2[j])
        return ans