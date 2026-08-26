class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k < 1:
            return []

        ans = []
        l = 0
        r = k - 1
        largest = nums[0]

        while r < len(nums):
            window = nums[l:r + 1]
            window_max = max(window)
            ans.append(window_max)
            l += 1
            r += 1

        return ans