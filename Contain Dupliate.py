class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        # Create a set to store the values within the current window
        window = set()
        
        for i, num in enumerate(nums):
            if num in window:
                return True  # Found a duplicate within the range
            window.add(num)
            # Remove the element that is out of the range
            if len(window) > k:
                window.remove(nums[i - k])
        
        return False  # No duplicate found within the range

# Example usage:
solution = Solution()
print(solution.containsNearbyDuplicate([1, 2, 3, 1], 3))  
print(solution.containsNearbyDuplicate([1, 0, 1, 1], 1))  
print(solution.containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2))  
