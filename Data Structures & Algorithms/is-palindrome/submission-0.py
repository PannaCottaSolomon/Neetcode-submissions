class Solution:
    def isPalindrome(self, s: str) -> bool:
        stc = "".join([c for c in s if c.isalnum()]).lower()
        ptr1 = 0
        ptr2 = len(stc) - 1
        print(stc)
        while ptr1 < ptr2:
            if stc[ptr1] != stc[ptr2]:
                return False
            ptr1 += 1
            ptr2 -= 1

        return True