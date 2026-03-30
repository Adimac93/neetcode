class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            row_unique = set()
            col_unique = set()
            box_unique = set()
            for j in range(len(board)):
                x = j % 3 + i % 3 * 3
                y = i % 3 + j // 3
                if board[y][x].isdigit() and board[y][x] in box_unique:
                    return False
                else:
                    box_unique.add(board[y][x])
                if board[i][j].isdigit() and board[i][j] in row_unique:
                    return False
                else:
                    row_unique.add(board[i][j])
                if board[j][i].isdigit() and board[j][i] in col_unique:
                    return False
                else:
                    col_unique.add(board[j][i])
            
        return True
            


        