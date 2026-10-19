class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) < 2:
            return ""
        
        longest = ""
        i = 0
        first = strs[0]
        rest = strs[1:]

        while i < len(first):
            char = first[i]
            for word in rest:
                if word[i] != char:
                    return longest
                
            longest += char
            i += 1

        return longest