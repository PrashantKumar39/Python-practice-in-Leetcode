class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        
        # Step 1: Determine if the first row or first column need to be zeroed
        first_row_zero = any(matrix[0][j] == 0 for j in range(n))
        first_col_zero = any(matrix[i][0] == 0 for i in range(m))
        
        # Step 2: Use the first row and first column as markers
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        # Step 3: Zero out cells based on the markers
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        # Step 4: Zero out the first row if necessary
        if first_row_zero:
            for j in range(n):
                matrix[0][j] = 0
        
        # Step 5: Zero out the first column if necessary
        if first_col_zero:
            for i in range(m):
                matrix[i][0] = 0

# Example usage:
solution = Solution()
matrix1 = [[1,1,1],[1,0,1],[1,1,1]]
solution.setZeroes(matrix1)
print(matrix1)  

matrix2 = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
solution.setZeroes(matrix2)
print(matrix2)  
 
