class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 0
        count = k
        longest = 0
        char = s[0]

        while left < len(s) and right < len(s):
            if right == 0:
                right += 1
                continue
            char = s[left]

            if s[right] == s[left]:
                right += 1
            else:
                if count > 0:
                    count -= 1
                    right += 1
                else:
                    while s[left] == char:
                        left += 1
                    left += 1
                    char = s[left]
                    count += 1
            longest = max(longest, right - left)
            
 

        return longest