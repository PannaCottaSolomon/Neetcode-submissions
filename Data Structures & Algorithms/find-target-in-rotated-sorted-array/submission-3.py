class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            return 0 if target == nums[0] else -1

        l = 0
        r = len(nums) - 1
        ans = -1

        while l < r:
            m = (l + r) // 2
            numL = nums[l]
            numR = nums[r]
            numM = nums[m]

            if numL > numR:
                if numL < target < numM:
                    r = m
                else:
                    l = m
            else:
                if target < numM:
                    r = m
                elif target > numM:
                    l = m + 1
                else:
                    return m
            # print(l, m, r, target)
        
        if l == r and target == nums[l]:
            return l
        return ans