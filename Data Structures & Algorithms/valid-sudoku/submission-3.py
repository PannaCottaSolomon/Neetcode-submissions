from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_map = defaultdict(list)
        col_map = defaultdict(list)
        quad_map = defaultdict(list)

        for i, row in enumerate(board):
            for j, cell in enumerate(row):
                # print(cell)
                if cell == ".":
                    continue

                col_idx = j // 3
                row_idx = i // 3
                quad_idx = row_idx * 3 + col_idx

                row_map[i].append(cell)
                col_map[j].append(cell)
                quad_map[quad_idx].append(cell)

        for key, value in row_map.items():
            count = len(value)
            set_count = len(set(value))
            if count != set_count:
                return False

        for key, value in col_map.items():
            count = len(value)
            set_count = len(set(value))
            if count != set_count:
                return False

        for key, value in quad_map.items():
            count = len(value)
            set_count = len(set(value))
            if count != set_count:
                return False

        return True