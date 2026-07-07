class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # define 2 hashmaps for each string.

        mapS, mapT = Counter(s), Counter(t)

        return mapS == mapT