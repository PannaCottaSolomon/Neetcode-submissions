class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = ["a", "e", "i", "o", "u"]
        vowel_strings = []
        queries_len = len(queries)
        ans = [-1] * queries_len

        for word in words:
            if word[0] in vowels and word[-1] in vowels:
                vowel_strings.append(True)
            else:
                vowel_strings.append(False)

        for i, query in enumerate(queries):
            left = query[0]
            right = query[1]
            count = 0
            for flag in vowel_strings[left : right + 1]:
                if flag:
                    count += 1
            ans[i] = count

        return ans