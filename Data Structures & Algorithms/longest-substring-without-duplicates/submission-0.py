class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = ""
        seen = []
        temp = ""
        for i, char in enumerate(s):
            if char not in seen:
                seen.append(char)
                temp += char
                if temp > longest:
                    longest = temp
            else:
                idx = temp.index(char)
                temp = temp[idx + 1:] + char
                

        return len(longest)