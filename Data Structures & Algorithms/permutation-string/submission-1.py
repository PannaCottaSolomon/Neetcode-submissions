class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        word_og = [char for char in s1]

        left = 0
        while left < len(s2):
            word = word_og.copy()
            right = left

            while right < len(s2) and s2[right] in word:
                letter = s2[right]
                word.remove(letter)
                right += 1
            
            if len(word) == 0:
                return True

            left += 1

        return False