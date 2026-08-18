class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0
        for i, char in enumerate(s):
            if i == 0:
                continue
            
            diff = abs(ord(char) - ord(s[i - 1]))
            score += diff

        return score