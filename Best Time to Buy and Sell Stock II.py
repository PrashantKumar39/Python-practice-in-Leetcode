class Solution:
    def maxProfit(self, prices):
        total_profit = 0
        
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                total_profit += prices[i] - prices[i - 1]
        
        return total_profit


sol = Solution()

# Example 1
prices1 = [7, 1, 5, 3, 6, 4]
print(sol.maxProfit(prices1))  

# Example 2
prices2 = [1, 2, 3, 4, 5]
print(sol.maxProfit(prices2))  

# Example 3
prices3 = [7, 6, 4, 3, 1]
print(sol.maxProfit(prices3)) 
