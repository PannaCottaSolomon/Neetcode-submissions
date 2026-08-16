class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []

        for i, num in enumerate(nums):
            remainder = target - num
            if remainder in nums:
                idx1 = i
                idx2 = nums.index(remainder)
                res.append(idx1)
                res.append(idx2)
                break

        return res