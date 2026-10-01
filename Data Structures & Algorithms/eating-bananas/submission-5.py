import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles) == h:
            return max(piles)

        upper = max(piles)
        lower = 1

        while lower < upper:
            mid = (upper + lower) // 2
            total_hours = 0
            for pile in piles:
                hours = math.ceil(pile / mid)
                total_hours += hours
            
            if total_hours < h:
                upper = mid
            elif total_hours > h:
                lower = mid + 1
            else:
                return mid

        return upper