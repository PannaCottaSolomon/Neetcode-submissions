class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        ptr1 = 0
        ptr2 = 0
        while ptr1 < len(s):
            s_char = s[ptr1]
            while ptr2 < len(t):
                if s_char == t[ptr2]:
                    break
                else:
                    ptr2 += 1

            if ptr2 >= len(t):
                return False

            ptr1 += 1

        return True