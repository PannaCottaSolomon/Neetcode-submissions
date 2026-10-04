class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        start = 0
        replacements = 0

        while start < len(s) - 1:
            currChar = s[start]
            end = start
            while end < len(s):
                # print(s[start:end + 1], replacements)
                if s[end] != currChar and replacements < k:
                    replacements += 1
                    end += 1
                elif s[end] == currChar:
                    end += 1
                else:
                    break

            longest = max(longest, end - start)
            replacements = 0
            start += 1

        return longest