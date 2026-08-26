class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        l = 0
        r = 0

        while r < len(nums):
            window = nums[l:r + 1]
            # print(window)
            largest = max(window)
            if r - l + 1 == k:
                ans.append(largest)
                l += 1
                r += 1
            else:
                r += 1

        return ans