class Solution:
    def search(self, nums: List[int], target: int) -> int:
        mid_idx = int(len(nums) / 2)
        mid = nums[mid_idx]

        if len(nums) == 1 and nums[0] != target:
            return -1

        # print(nums)
        if target > mid:
            self.search(nums[mid_idx:], target)
        elif target < mid:
            self.search(nums[:mid_idx], target)
        elif target == mid:
            return mid_idx

        return -1
