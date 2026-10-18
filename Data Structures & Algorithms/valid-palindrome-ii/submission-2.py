from collections import defaultdict

class Solution:
    def validPalindrome(self, s: str) -> bool:
        if len(s) == 1:
            return True

        counts = defaultdict(int)
        for char in s:
            counts[char] += 1

        unique = 0
        for char, counts in counts.items():
            if counts == 1:
                unique += 1

        return True if unique < 2 or len(s) <= 2 else False