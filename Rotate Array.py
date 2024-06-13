class Solution:
    def rotate(self, nums, k):
        n = len(nums)
        k = k % n  # Normalize k

        # Helper function to reverse a sublist in-place
        def reverse(nums, start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        # Reverse the entire array
        reverse(nums, 0, n - 1)
        # Reverse the first k elements
        reverse(nums, 0, k - 1)
        # Reverse the remaining n - k elements
        reverse(nums, k, n - 1)

# Example usage
sol = Solution()

# Example 1
nums1 = [1, 2, 3, 4, 5, 6, 7]
k1 = 3
sol.rotate(nums1, k1)
print(nums1)  

# Example 2
nums2 = [-1, -100, 3, 99]
k2 = 2
sol.rotate(nums2, k2)
print(nums2)  
