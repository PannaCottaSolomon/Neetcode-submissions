class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        for i, num in enumerate(nums):
            if num not in frequency:
                frequency[num] = 1
            else:
                frequency[num] += 1

        sorted_freq = dict(sorted(frequency.items(), key=lambda item: item[1], reverse=True))

        result = []
        for number, count in sorted_freq.items():
            result.append(number)

        return result[:k]