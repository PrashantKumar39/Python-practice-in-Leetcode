class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        
        write_index = 1
        
        for i in range(1, len(nums)):
            if nums[i] != nums[write_index - 1]:
                nums[write_index] = nums[i]
                write_index += 1
        
        return write_index

# Example usage
sol = Solution()

# Example 1
nums1 = [1, 1, 2]
k1 = sol.removeDuplicates(nums1)
print(k1, nums1[:k1])  # Output: 2, [1, 2]

# Example 2
nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
k2 = sol.removeDuplicates(nums2)
print(k2, nums2[:k2])  # Output: 5, [0, 1, 2, 3, 4]
