class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = []
        for i, letter in enumerate(s):
            if letter.isalnum():
                cleaned.append(letter)

        cleaned_string = "".join(cleaned).lower()
        reverse = "".join(reversed(cleaned_string))

        return reverse == cleaned_string