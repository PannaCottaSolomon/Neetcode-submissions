class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        setNums = set(nums)
        # print(len(setNums))
        # print(len(nums))
        return len(setNums) != len(nums)