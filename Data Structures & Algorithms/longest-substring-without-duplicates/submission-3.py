class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = ""
        temp = ""
        for i, char in enumerate(s):
            if char not in temp:
                temp += char
            else:
                idx = temp.index(char)
                temp = temp[idx + 1:] + char
            if len(temp) > len(longest):
                longest = temp
                
        return len(longest)