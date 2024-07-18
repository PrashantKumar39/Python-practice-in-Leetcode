class Solution:
    def gameOfLife(self, board: list[list[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        
        rows, cols = len(board), len(board[0])
        
        def count_live_neighbors(r, c):
            live_neighbors = 0
            for i in range(max(0, r-1), min(rows, r+2)):
                for j in range(max(0, c-1), min(cols, c+2)):
                    if (i, j) != (r, c):
                        live_neighbors += board[i][j] & 1
            return live_neighbors
        
        for r in range(rows):
            for c in range(cols):
                live_neighbors = count_live_neighbors(r, c)
                if board[r][c] == 1 and (live_neighbors == 2 or live_neighbors == 3):
                    board[r][c] |= 2  # Mark as live in the next state
                if board[r][c] == 0 and live_neighbors == 3:
                    board[r][c] |= 2  # Mark as live in the next state
        
        for r in range(rows):
            for c in range(cols):
                board[r][c] >>= 1  # Update to the next state

# Example usage:
solution = Solution()
board1 = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
solution.gameOfLife(board1)
print(board1)  

board2 = [[1,1],[1,0]]
solution.gameOfLife(board2)
print(board2)  
