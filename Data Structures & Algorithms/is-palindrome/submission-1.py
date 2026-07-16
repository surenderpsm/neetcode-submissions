class Solution:
    def isPalindrome(self, s: str) -> bool:
        # clean up s

        s = s.lower()


        x, y = 0, len(s)-1


        while x < y:
            while not s[x].isalnum() and x < y:
                x+=1
            while not s[y].isalnum() and x < y:
                y-=1
            
            if s[x] != s[y]:
                return False
            
            x+=1
            y-=1
        
        return True

# abba  

# clean up palindrome. remove spaces, and lowercase everything.

# can be both even or odd palindrome.

# abcba - odd - place pointer in first and last. compare equality with while loop, if loop fails, not a palindrome.
# while end condition is when index are equal.

# abba - even - place pointer in first and last. compare till one plus one