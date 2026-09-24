class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsUnique = list(set(nums))
        numsUnique.sort()
        if len(numsUnique) < 2:
            return len(numsUnique)

        # print(numsUnique)
        longest = 0
        count = 1

        for i, num in enumerate(numsUnique):
            if i == 0:
                continue 
            
            if num == numsUnique[i - 1] + 1:
                count += 1
                # print(count)
            else:
                # print(longest)
                longest = max(longest, count)
                count = 1

            longest = max(longest, count)

        return longest