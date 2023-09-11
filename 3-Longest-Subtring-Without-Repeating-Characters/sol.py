class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i,j=0,0
        _max=0
        hashSet=set({})
        while(j<len(s)):
            if s[j] not in hashSet:
                hashSet.add(s[j])
                j+=1
                _max=max(len(hashSet),_max)
            else:
                hashSet.remove(s[i])
                i+=1
        return _max
