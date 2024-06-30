class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # Pointer for s
        s_pointer = 0
        # Pointer for t
        t_pointer = 0
        
        # Loop through t to find characters of s in sequence
        while t_pointer < len(t):
            # If characters match, move s_pointer to the next character
            if s_pointer < len(s) and s[s_pointer] == t[t_pointer]:
                s_pointer += 1
            # Always move t_pointer to the next character
            t_pointer += 1
            
            # If s_pointer has reached the end of s, all characters were found
            if s_pointer == len(s):
                return True
        
        # If s_pointer has not reached the end of s, not all characters were found
        return s_pointer == len(s)

# Example usage
solution = Solution()
print(solution.isSubsequence("abc", "ahbgdc")) 
print(solution.isSubsequence("axc", "ahbgdc")) 
