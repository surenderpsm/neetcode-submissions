class Solution:
    def longestPalindrome(self, s: str) -> str:
        # This is 2 pointer problem not dp

        # 2 cases: odd and even palindromes

        res = ""
        resLen = 0

        for i in range(len(s)):

            # odd
            l,r = i,i
            while l >= 0 and r < len(s) and s[r] == s[l]:
                if resLen < r-l+1:
                    res = s[l:r+1]
                    resLen = r-l+1
                l-=1
                r+=1
            
            # even
            l,r = i,i+1
            while l >= 0 and r<len(s) and s[r] == s[l]:
                if resLen < r-l+1:
                    res = s[l:r+1]
                    resLen = r - l + 1
                l-=1
                r+=1

        return res


# remember about slicing and playing around with indices.
# rememebr that to find palindrom wwe can go from ends to meet or from center outwards which is more efficient