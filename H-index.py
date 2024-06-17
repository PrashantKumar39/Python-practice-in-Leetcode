class Solution:
    def hIndex(self, citations):
        citations.sort(reverse=True)
        h_index = 0
        for i, c in enumerate(citations):
            if i + 1 <= c:
                h_index = i + 1
            else:
                break
        return h_index

sol = Solution()

# Example 1
citations1 = [3, 0, 6, 1, 5]
print(sol.hIndex(citations1))  

# Example 2
citations2 = [1, 3, 1]
print(sol.hIndex(citations2))  
