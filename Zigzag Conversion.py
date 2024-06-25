class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # Edge case
        if numRows == 1 or numRows >= len(s):
            return s

        # Initialize a list of empty strings for each row
        rows = [''] * numRows
        current_row = 0
        going_down = False

        # Iterate through the characters in the string
        for char in s:
            rows[current_row] += char
            # Change direction at the top and bottom row
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down
            current_row += 1 if going_down else -1

        # Join all rows to form the final string
        return ''.join(rows)

# Example usage
solution = Solution()
print(solution.convert("PAYPALISHIRING", 3))  
print(solution.convert("PAYPALISHIRING", 4))  
print(solution.convert("A", 1))               
