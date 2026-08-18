class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        idx = -1
        for i, character in enumerate(s):
            if character in t and s.index(character) > idx:
                idx = s.index(character)
            else:
                return False

        return True