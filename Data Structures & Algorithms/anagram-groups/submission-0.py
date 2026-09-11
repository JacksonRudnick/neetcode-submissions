class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        t = {}
        
        for s in strs:
            tmp = str(sorted(s))
            if not tmp in t:
                t[tmp] = [s]
            else:
                t[tmp] += [s]

        return list(t.values())