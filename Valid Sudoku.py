class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # Initialize sets for rows, columns, and sub-boxes
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue
                
                # Determine the index of the sub-box
                box_index = (r // 3) * 3 + (c // 3)
                
                # Check if the value is already in the corresponding row, column, or sub-box
                if val in rows[r] or val in cols[c] or val in boxes[box_index]:
                    return False
                
                # Add the value to the corresponding row, column, and sub-box
                rows[r].add(val)
                cols[c].add(val)
                boxes[box_index].add(val)
        
        return True

# Example usage
solution = Solution()
board1 = [["5","3",".",".","7",".",".",".","."]
         ,["6",".",".","1","9","5",".",".","."]
         ,[".","9","8",".",".",".",".","6","."]
         ,["8",".",".",".","6",".",".",".","3"]
         ,["4",".",".","8",".","3",".",".","1"]
         ,["7",".",".",".","2",".",".",".","6"]
         ,[".","6",".",".",".",".","2","8","."]
         ,[".",".",".","4","1","9",".",".","5"]
         ,[".",".",".",".","8",".",".","7","9"]]
board2 = [["8","3",".",".","7",".",".",".","."]
         ,["6",".",".","1","9","5",".",".","."]
         ,[".","9","8",".",".",".",".","6","."]
         ,["8",".",".",".","6",".",".",".","3"]
         ,["4",".",".","8",".","3",".",".","1"]
         ,["7",".",".",".","2",".",".",".","6"]
         ,[".","6",".",".",".",".","2","8","."]
         ,[".",".",".","4","1","9",".",".","5"]
         ,[".",".",".",".","8",".",".","7","9"]]

print(solution.isValidSudoku(board1))  
print(solution.isValidSudoku(board2))  
