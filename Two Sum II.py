from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        
        while left < right:
            current_sum = numbers[left] + numbers[right]
            if current_sum == target:
                return [left + 1, right + 1]  # Return 1-based indices
            elif current_sum < target:
                left += 1
            else:
                right -= 1
        
        return []  

# Example usage
solution = Solution()
print(solution.twoSum([2, 7, 11, 15], 9))  
print(solution.twoSum([2, 3, 4], 6))       
print(solution.twoSum([-1, 0], -1))       
