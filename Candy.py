class Solution:
    def candy(self, ratings):
        n = len(ratings)
        if n == 0:
            return 0
        
        # Initialize candies array with 1 candy for each child
        candies = [1] * n
        
        # Left to right pass
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1
        
        # Right to left pass
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)
        
        # Sum up the candies
        return sum(candies)

# Example Usage
solution = Solution()
print(solution.candy([1, 0, 2]))  
print(solution.candy([1, 2, 2]))  
