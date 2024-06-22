class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Strip trailing spaces and split the string into words
        words = s.strip().split()
        # Return the length of the last word
        return len(words[-1])

# Creating an instance of the Solution class
solution = Solution()

# Example 1
s1 = "Hello World"
print(solution.lengthOfLastWord(s1))  

# Example 2
s2 = "   fly me   to   the moon  "
print(solution.lengthOfLastWord(s2))  

# Example 3
s3 = "luffy is still joyboy"
print(solution.lengthOfLastWord(s3))  
