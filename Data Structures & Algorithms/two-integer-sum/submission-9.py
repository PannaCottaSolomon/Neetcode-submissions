class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []

        for i, num in enumerate(nums):
            remainder = target - num
            if remainder in nums:
                idx1 = i
                res.append(idx1)

                nums2 = nums[i + 1:]
                idx2 = nums2.index(remainder)
                idx2 += i + 1
                res.append(idx2)
                break

        return res