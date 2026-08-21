class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        word = [char for char in s1]

        left = 0
        right = 0
        while left < len(s2):
            right = left
            while s2[right] in word:
                letter = s2[right]
                word.remove(letter)
                right += 1
                # print(word)
            
            if len(word) == 0:
                return True
            else:
                word = [char for char in s1]

            left += 1

        return False