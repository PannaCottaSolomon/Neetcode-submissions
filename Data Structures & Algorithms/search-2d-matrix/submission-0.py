class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        bottom = len(matrix) - 1

        while top <= bottom:
            mid = (top + bottom) // 2

            if target > matrix[mid][-1]:
                top = mid + 1
            elif target < matrix[mid][0]:
                bottom = mid - 1
            else:
                # target must be somewhere in this row
                break

        if top > bottom:
            return False

        row = matrix[mid]

        l = 0
        r = len(row) - 1

        while l <= r:
            m = (l + r) // 2

            if target > row[m]:
                l = m + 1
            elif target < row[m]:
                r = m - 1
            else:
                return True

        return False