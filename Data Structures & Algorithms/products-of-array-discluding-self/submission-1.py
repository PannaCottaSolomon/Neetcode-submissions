class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = []
        right = []

        for i, num in enumerate(nums):
            if i == 0:
                left.append(1 * num)
            else:
                total = left[i - 1] * num
                left.append(total)
        # print(left)

        reverse = list(reversed(nums))
        # print(reverse)
        for j, num in enumerate(reverse):
            if j == 0:
                right.append(1 * num)
            else:
                total2 = right[j - 1] * num
                right.append(total2)
        # print(right)

        right.reverse()
        product = []
        for i in range(len(nums)):
            l = i - 1
            r = i + 1
            if l < 0:
                product.append(1 * right[r])
            elif r > len(nums) - 1:
                product.append(1 * left[l])
            else:
                product.append(left[l] * right[r])

        return product