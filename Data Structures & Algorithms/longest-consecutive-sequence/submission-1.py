class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        nums.sort()
        nums_unique = list(set(nums))
        # print(nums_unique)

        longest = 0
        count = 1
        for i, num in enumerate(nums_unique):
            if i == 0:
                continue
            
            if num == nums_unique[i - 1] + 1:
                count += 1
            else:
                if count > longest:
                    longest = count
                count = 1

        if count > longest:
            longest = count

        return longest