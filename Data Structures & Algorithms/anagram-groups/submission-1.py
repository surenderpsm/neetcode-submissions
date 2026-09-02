class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        map = defaultdict(list)

        for s in strs:

            fingerprint = [0] * 26

            for c in s:
                fingerprint[ord(c)-ord('a')] +=1
            
            map[tuple(fingerprint)].append(s)
        res = []
        for l in map.values():
            res.append(l)
        
        return res