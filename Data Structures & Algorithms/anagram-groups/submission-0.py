class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        anagrams = {}

        for word in strs:
            w = "".join(sorted(word))
            if w not in anagrams.keys():
                anagrams[w] = [word]
            else:
                existing_words = anagrams[w]
                existing_words.append(word)
                anagrams[w] = existing_words
        
        for key, value in anagrams.items():
            result.append(value)

        return result