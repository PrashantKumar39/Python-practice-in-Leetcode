class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)

solution = Solution()
print(solution.strStr("sadbutsad", "sad"))  
print(solution.strStr("leetcode", "leeto"))
