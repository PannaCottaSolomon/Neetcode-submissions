class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        l = 0
        r = k - 1
        largest = nums[0]

        while r < len(nums):
            window = nums[l:r + 1]
            window_max = max(window)
            largest = max(largest, window_max)
            ans.append(largest)
            l += 1
            r += 1

        return ans