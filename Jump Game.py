class Solution:
    def canJump(self, nums):
        max_reach = 0
        for i in range(len(nums)):
            if i > max_reach:
                return False
            max_reach = max(max_reach, i + nums[i])
            if max_reach >= len(nums) - 1:
                return True
        return False

sol = Solution()

# Example 1
nums1 = [2, 3, 1, 1, 4]
print(sol.canJump(nums1))  

# Example 2
nums2 = [3, 2, 1, 0, 4]
print(sol.canJump(nums2))  
