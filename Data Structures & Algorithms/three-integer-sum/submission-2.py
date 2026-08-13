class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []
        nums.sort()
        print(nums)

        for i, n1 in enumerate(nums):
            if i > 0 and n1 == nums[i - 1]:
                continue

            target = 0 - n1
            print("target:", target)
            
            l, r = i + 1, len(nums) - 1
            while l < r:
                total = nums[l] + nums[r]
                if total == target:
                    results.append([n1, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                elif total < target:
                    l += 1
                else:
                    r -= 1
                
        return results