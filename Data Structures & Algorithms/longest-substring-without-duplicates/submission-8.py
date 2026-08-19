class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = []
        longest = 0

        for i, char in enumerate(s):
            if char not in window:
                window.append(char)
            else:                
                idx_duplicate = window.index(char)
                del window[:idx_duplicate + 1]
                window.append(char)

            # print(window)
            longest = max(longest, len(window))

        return longest