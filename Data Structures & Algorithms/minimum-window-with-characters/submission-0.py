class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        r = 0
        ans = s
        substring = ""
        t_list = [char for char in t]

        while l < len(s):
            # print(t_list)
            if s[l] not in t_list:
                l += 1
                continue

            r = l
            while r < len(s) and t_list:
                if s[r] in t_list:
                    t_list.remove(s[r])
                r += 1

            if not t_list:
                substring = s[l:r]
            if len(substring) < len(ans):
                ans = substring

        return ans