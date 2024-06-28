class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Normalize the string by converting to lowercase and filtering non-alphanumeric characters
        filtered_chars = [char.lower() for char in s if char.isalnum()]
        normalized_str = ''.join(filtered_chars)
        
        # Check if the normalized string is equal to its reverse
        return normalized_str == normalized_str[::-1]

# Example usage
solution = Solution()
print(solution.isPalindrome("A man, a plan, a canal: Panama"))  
print(solution.isPalindrome("race a car")) 
print(solution.isPalindrome(" "))  
