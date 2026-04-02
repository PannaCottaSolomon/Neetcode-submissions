class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        existing = []
        for i, num in enumerate(nums):
            if num in existing:
                return True
            else:
                existing.append(num)
        return False