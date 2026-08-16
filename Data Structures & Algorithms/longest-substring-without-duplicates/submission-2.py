class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = ""
        seen = set()
        temp = ""
        for i, char in enumerate(s):
            if char not in seen:
                seen.add(char)
                temp += char
                if temp > longest:
                    longest = temp
            else:
                idx = temp.index(char)
                temp = temp[idx + 1:] + char
                seen = set(temp)
            
            print(seen)
            print(temp)
                

        return len(longest)