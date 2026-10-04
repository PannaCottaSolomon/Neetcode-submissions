class Solution:
    def rob(self, nums: List[int]) -> int:
        profits = [0] * len(nums)

        for i in range(len(nums)):
            if i == 0:
                profits[i] = nums[i]
            elif i == 1:
                profits[i] = max(nums[1], nums[0])
            else:
                curr = nums[i]
                profits[i] = max(curr + profits[i - 2], profits[i - 1])
            # print(profits)


        return profits[-1]