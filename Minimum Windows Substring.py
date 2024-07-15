from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        
        # Dictionary which keeps a count of all the unique characters in t.
        dict_t = Counter(t)
        
        # Number of unique characters in t that must be present in the desired window.
        required = len(dict_t)
        
        # Left and Right pointer
        left, right = 0, 0
        
        # Formed is used to keep track of how many unique characters in t
        # are present in the current window in the desired frequency.
        formed = 0
        
        # Dictionary which keeps a count of all the unique characters in the current window.
        window_counts = {}
        
        # (window length, left, right)
        ans = float("inf"), None, None
        
        while right < len(s):
            # Add one character from the right to the window
            character = s[right]
            window_counts[character] = window_counts.get(character, 0) + 1
            
            # If the frequency of the current character added equals to the desired count in t
            # then increment the formed count by 1.
            if character in dict_t and window_counts[character] == dict_t[character]:
                formed += 1
            
            # Try and contract the window till the point where it ceases to be 'desirable'.
            while left <= right and formed == required:
                character = s[left]
                
                # Save the smallest window until now.
                if right - left + 1 < ans[0]:
                    ans = (right - left + 1, left, right)
                
                # The character at the position pointed by the `left` pointer is no longer a part of the window.
                window_counts[character] -= 1
                if character in dict_t and window_counts[character] < dict_t[character]:
                    formed -= 1
                
                # Move the left pointer ahead, this would help to look for a new window.
                left += 1
            
            # Keep expanding the window once we are done contracting.
            right += 1
        
        return "" if ans[0] == float("inf") else s[ans[1]: ans[2] + 1]

# Example usage
solution = Solution()
print(solution.minWindow("ADOBECODEBANC", "ABC"))  # Output: "BANC"
print(solution.minWindow("a", "a"))  # Output: "a"
print(solution.minWindow("a", "aa"))  # Output: ""
