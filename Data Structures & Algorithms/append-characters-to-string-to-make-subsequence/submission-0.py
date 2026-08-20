class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        count = 0
        ptr = 0
        for i, letter in enumerate(t):
            while ptr < len(s) and s[ptr] != letter:
                # print(s[ptr])
                ptr += 1
            
            if ptr < len(s) and s[ptr] == letter:
                ptr += 1
                continue
            else:
                count = len(t) - i
                break

        return count