class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles) == h:
            return max(piles)

        for height in range(1, h):
            counts = []
            for num in piles:
                if num <= height:
                    counts.append(1)
                else:
                    repeats = (num // height) + 1 if num % height > 0 else num // height
                    counts.append(repeats)
            
            total = sum(counts)
            if total <= h:
                return height

        return 1