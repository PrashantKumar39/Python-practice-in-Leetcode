from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        anagrams = defaultdict(list)
        
        for s in strs:
            sorted_s = tuple(sorted(s))
            anagrams[sorted_s].append(s)
        
        return list(anagrams.values())

# Example usage:
solution = Solution()
print(solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))  
print(solution.groupAnagrams([""]))                                   
print(solution.groupAnagrams(["a"]))                                  
