from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        start = 0
        end = start
        frequencies = defaultdict(int)

        while end < len(s):
            currChar = s[end]
            frequencies[currChar] += 1
            maxf = max(frequencies.values())

            while (end - start + 1) - maxf > k:
                frequencies[s[start]] -= 1
                start += 1

            longest = max(longest, end - start + 1)
            end += 1

        return longest