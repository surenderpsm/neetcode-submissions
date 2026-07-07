class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # map of lists. we add anagrams to it as we find them
        # what is the key of the map.maybe the first word we find. to start the list
        # no, use a tuple of 26 letters as a key.

        map = defaultdict(List)

        for str in strs:
            # create the tuple for string.
            fingerprint = [0] *26
            for char in str:
                fingerprint[ord(char) - ord('a')]+=1
            
            fingerprint = tuple(fingerprint)

            # add the string to fingerprint cluster
            if fingerprint in map:
                map[fingerprint].append(str)
            else:
                map[fingerprint] = [str]

        sol = []
        for cluster in map.values():
            sol.append(cluster)
        return sol
            