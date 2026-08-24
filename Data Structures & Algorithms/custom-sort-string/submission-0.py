class Solution:
    def customSortString(self, order: str, s: str) -> str:
        overlaps = {}
        ans = ""

        for i, letter in enumerate(order):
            if letter in s:
                overlaps[i] = letter
        
        for key, value in overlaps.items():
            while value in s:
                s = s.replace(value, "", 1)
                ans += value

        return ans + s