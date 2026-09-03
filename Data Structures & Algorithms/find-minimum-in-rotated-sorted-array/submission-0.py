class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        while l < r:
            mid = (l + r) // 2
            num_left = nums[l]
            num_mid = nums[mid]
            num_right = nums[r]

            if num_left > num_right:
                if num_left < num_mid:
                    l = mid + 1
                elif num_mid < num_right:
                    r = mid
                else:
                    break
            else:
                if num_left < num_mid:
                    r = mid - 1

        return nums[r]