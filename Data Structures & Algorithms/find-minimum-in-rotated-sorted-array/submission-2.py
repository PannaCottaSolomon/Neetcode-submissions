class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        m = (l + r) // 2

        while l < r:
            left = nums[l]
            mid = nums[m]
            right = nums[r]

            if left > right:
                l = m
            else:
                r = m
            m = (l + r) // 2

            

        return left