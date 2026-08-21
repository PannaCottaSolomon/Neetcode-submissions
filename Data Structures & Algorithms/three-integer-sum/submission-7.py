class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []
        nums.sort()

        for i, num in enumerate(nums):
            if i > 0 and num == nums[i - 1]:
                continue
            target = 0 - num
            # print("target: ", target)
            remainder = nums[i + 1:]

            left = 0
            right = len(remainder) - 1
            while left < right:
                num_j = remainder[left]
                num_k = remainder[right]
                # print("numJ: ", num_j)
                # print("numK: ", num_k)
                total = num_j + num_k

                if total == target:
                    results.append([num, num_j, num_k])
                    left += 1
                elif total > target:
                    right -= 1
                elif total < target:
                    left += 1
                

        return results