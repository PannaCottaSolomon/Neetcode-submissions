class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {}
        cols = {}
        sqrs = {}

        for rowIdx, row in enumerate(board):
            for colIdx, num in enumerate(row):
                if num == ".":
                    continue

                if rowIdx not in rows.keys():
                    rows[rowIdx] = [num]
                else:
                    old = rows[rowIdx]
                    if num in old:
                        return False
                    old.append(num)
                    rows[rowIdx] = old

                if colIdx not in cols.keys():
                    cols[colIdx] = [num]
                else:
                    old = cols[colIdx]
                    if num in old:
                        return False
                    old.append(num)
                    cols[colIdx] = old

                sqrIdx = (rowIdx // 3) * 3 + (colIdx // 3)
                if sqrIdx not in sqrs.keys():
                    sqrs[sqrIdx] = [num]
                else:
                    old = sqrs[sqrIdx]
                    if num in old:
                        return False
                    old.append(num)
                    sqrs[sqrIdx] = old
        

        return True