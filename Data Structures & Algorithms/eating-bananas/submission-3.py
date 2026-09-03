class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles) == h:
            return max(piles)
        elif len(piles) == 1:
            return piles[0]

        piles.sort()
        # print(piles)
        ans = max(piles)
        for height in range(ans, 1, -1):
            # print(height)
            counts = []
            for num in piles:
                if num <= height:
                    counts.append(1)
                else:
                    repeats = (num // height) + 1 if num % height > 0 else num // height
                    counts.append(repeats)
            
            # print(counts)
            total = sum(counts)
            if total <= h:
                ans = height
            else:
                break

        return ans