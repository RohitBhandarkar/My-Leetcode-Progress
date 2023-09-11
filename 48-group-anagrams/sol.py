from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for i in strs:
            ans[str(sorted(i))].append(i)
        res = list(ans.values())
        return res