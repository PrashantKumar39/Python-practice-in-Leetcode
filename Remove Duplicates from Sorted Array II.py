class Solution:
    def removeDuplicates(self, nums):
        if len(nums) <= 2:
            return len(nums)
        
        write_index = 1
        count = 1
        
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                count += 1
            else:
                count = 1
            
            if count <= 2:
                nums[write_index] = nums[i]
                write_index += 1
        
        return write_index

# Example usage
sol = Solution()

# Example 1
nums1 = [1, 1, 1, 2, 2, 3]
k1 = sol.removeDuplicates(nums1)
print(k1, nums1[:k1])  

# Example 2
nums2 = [0, 0, 1, 1, 1, 1, 2, 3, 3]
k2 = sol.removeDuplicates(nums2)
print(k2, nums2[:k2])  
