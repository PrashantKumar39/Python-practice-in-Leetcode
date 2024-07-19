from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Count the occurrences of each character in the magazine and ransom note
        magazine_count = Counter(magazine)
        ransom_note_count = Counter(ransomNote)
        
        # Check if each character in the ransom note can be found in the magazine in sufficient quantity
        for char, count in ransom_note_count.items():
            if magazine_count[char] < count:
                return False
        return True

# Example usage:
solution = Solution()
print(solution.canConstruct("a", "b"))          # Output: False
print(solution.canConstruct("aa", "ab"))        # Output: False
print(solution.canConstruct("aa", "aab"))       # Output: True
