class Solution:
    def search(self, nums: List[int], target: int) -> int:
        original = nums
        while len(nums) > 1:
            halfIdx = int(len(nums) / 2)
            half = nums[halfIdx]
            print(half)
            if target > half:
                nums = nums[halfIdx:]
            elif target < half:
                nums = nums[:halfIdx]
            else:
                return original.index(target)

        return -1