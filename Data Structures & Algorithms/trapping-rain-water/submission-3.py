class Solution:
    def trap(self, height: List[int]) -> int:
        prefix = []
        suffix = []
        highest = 0
        height_reverse = list(reversed(height))
        total = 0

        for i in range(len(height)):
            if height[i] > highest:
                highest = height[i]
            prefix.append(highest)
            # print("pre:", highest)

        highest = 0
        for j in range(len(height)):
            if height_reverse[j] > highest:
                highest = height_reverse[j]
            suffix.append(highest)
            # print("suf:", highest)
    
        suffix.reverse()
        # print(prefix)
        # print(suffix)
        for k, h in enumerate(height):
            if k == 0 or k == len(height) - 1:
                continue
            water_trapped = min(prefix[k], suffix[k]) - h
            if water_trapped > 0:
                total += water_trapped
            water_trapped = 0
        
        return total