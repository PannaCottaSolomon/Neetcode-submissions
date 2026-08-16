class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0
        left = 0
        right = -1

        while left < len(height):
            if height[left] == 0:
                left += 1
            
            blocked = 0
            leftHeight = height[left]

            right = left + 1
            rightHeight = height[right]
            while rightHeight < leftHeight and right < len(height) - 1:
                blocked += rightHeight
                right += 1
                rightHeight = height[right]
            
            if right == len(height) - 1:
                break

            base = right - left - 1
            total += min(leftHeight, rightHeight) * base - blocked
            left = right
            # print(total)


        return total