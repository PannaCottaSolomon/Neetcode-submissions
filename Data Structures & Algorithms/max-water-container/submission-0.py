class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxVol = 0
        left = 0
        right = len(heights) - 1

        while left < right:
            leftHeight = heights[left]
            rightHeight = heights[right]
            dist = right - left
            currVol = dist * min(leftHeight, rightHeight)
            print(currVol)
            if currVol > maxVol:
                maxVol = currVol

            if leftHeight < rightHeight:
                left += 1
            else:
                right -= 1

    
        return maxVol