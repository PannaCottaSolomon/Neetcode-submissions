class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_list = []
        for string in strs:
            length = len(string)
            encoded_list.append(f"length#{string}")
        
        return "∑".join(encoded_list)


    def decode(self, s: str) -> List[str]:
        decoded_list = s.split("∑")

        results = []
        for string in decoded_list:
            if string == "":
                return []
            delimiter_idx = string.index("#")
            length = string[:delimiter_idx]
            word = string[delimiter_idx + 1:]
            results.append(word)
        
        return results
