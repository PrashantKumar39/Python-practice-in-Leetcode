class Solution:
    def removeElement(self, nums, val):
        write_index = 0
        
        for i in range(len(nums)):
            if nums[i] != val:
                nums[write_index] = nums[i]
                write_index += 1
        
        return write_index

# Example usage
sol = Solution()

# Example 1
nums1 = [3, 2, 2, 3]
val1 = 3
new_length1 = sol.removeElement(nums1, val1)
print(new_length1, nums1[:new_length1])  # Output: 2, [2, 2]

# Example 2
nums2 = [0, 1, 2, 2, 3, 0, 4, 2]
val2 = 2
new_length2 = sol.removeElement(nums2, val2)
print(new_length2, nums2[:new_length2])  # Output: 5, [0, 1, 3, 0, 4]
