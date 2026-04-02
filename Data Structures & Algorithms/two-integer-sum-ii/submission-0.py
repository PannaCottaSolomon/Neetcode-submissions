class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        result = []
        for i, num in enumerate(numbers[:-1]):
            for j, num2 in enumerate(numbers[i + 1:]):
                if num + num2 == target:
                    result.append(i + 1)
                    result.append(j + 1 + i + 1)

        return result


