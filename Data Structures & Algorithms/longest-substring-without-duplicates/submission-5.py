class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 0
        currLen = 0
        seen = []

        for char in s:
            if char not in seen:
                seen.append(char)
                currLen += 1
            else:
                seen.clear()
                seen.append(char)
                # print(seen)
                currLen = 1
            
            maxLen = max(maxLen, currLen)
        return maxLen