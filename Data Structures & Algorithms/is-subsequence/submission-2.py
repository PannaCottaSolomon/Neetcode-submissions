class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        l = 0
        l2 = 0
        while l < len(s) and l2 < len(t):

            l2 = l
            while l2 < len(t):
                char_s = s[l]
                char_t = t[l2]
                # print("s", char_s)
                # print("t", char_t)
                if char_t == char_s:
                    l += 1
                    l2 += 1
                else:
                    l2 += 1
            l += 1

        if l >= len(s):
            return True
        return False
