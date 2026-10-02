class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        ans = []
        endings = {}
        for i, char in enumerate(s):
            endings[char] = i
        
        size = 0
        end = 0
        for i, char in enumerate(s):
            curr_end = endings[char]
            end = max(end, curr_end)
            size += 1

            if i == end:
                end = 0
                ans.append(size)
                size = 0

        return ans