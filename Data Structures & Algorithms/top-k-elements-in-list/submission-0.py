class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        repeats = {}

        for num in nums:
            if num not in repeats:
                repeats[num] = 1
            else:
                repeats[num] += 1

        sorted_repeats = dict(sorted(repeats.items(), key=lambda item: item[1], reverse=True))
        print(sorted_repeats)

        res = []
        i = 0
        for key in sorted_repeats.keys():
            if i < k:
                res.append(key)
                i += 1
            else:
                break

        return res