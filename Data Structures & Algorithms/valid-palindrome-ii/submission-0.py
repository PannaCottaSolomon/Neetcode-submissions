class Solution:
    def validPalindrome(self, s: str) -> bool:
        if len(s) == 1:
            return True

        count = 0
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                count += 1
            
            if count > 1:
                return False

            l += 1
            r -= 1


        return True