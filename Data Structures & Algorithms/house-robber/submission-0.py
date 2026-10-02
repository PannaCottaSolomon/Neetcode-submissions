class Solution:
    def rob(self, nums: List[int]) -> int:
        odd = 0
        even = 0
        for i, num in enumerate(nums):
            if i % 2 == 0:
                even += num
            else:
                odd += num

        return max(odd, even)