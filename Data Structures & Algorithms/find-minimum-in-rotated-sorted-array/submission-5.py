class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        m = (l + r) // 2
        left = nums[l]
        mid = nums[m]
        right = nums[r]

        while l < r:
            if left > right > mid:
                r = m
            elif mid > right:
                l = m + 1
            else:
                r = m

            m = (l + r) // 2

            left = nums[l]
            mid = nums[m]
            right = nums[r]

        return left