class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        
        # Initialize the left and right product arrays
        left_products = [1] * n
        right_products = [1] * n
        
        # Compute the left products
        for i in range(1, n):
            left_products[i] = left_products[i - 1] * nums[i - 1]
        
        # Compute the right products
        for i in range(n - 2, -1, -1):
            right_products[i] = right_products[i + 1] * nums[i + 1]
        
        # Compute the result
        result = [1] * n
        for i in range(n):
            result[i] = left_products[i] * right_products[i]
        
        return result

# Example Usage
solution = Solution()
print(solution.productExceptSelf([1, 2, 3, 4])) 
print(solution.productExceptSelf([-1, 1, 0, -3, 3]))  
