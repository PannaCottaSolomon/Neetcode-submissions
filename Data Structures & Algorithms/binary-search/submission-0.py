class Solution:
    def search(self, nums: List[int], target: int) -> int:
        halfIdx = int(len(nums) / 2)
        half = nums[halfIdx]
        if target > half:
            nums = nums[halfIdx:]
        elif target < half:
            nums = nums[:halfIdx]
        else:
            return halfIdx

        return -1