from collections import Counter

class Solution:
    def findSubstring(self, s: str, words):
        if not s or not words:
            return []
        
        word_length = len(words[0])
        total_length = word_length * len(words)
        word_count = Counter(words)
        
        result = []
        
        for i in range(len(s) - total_length + 1):
            substring = s[i:i + total_length]
            words_in_substring = [substring[j:j + word_length] for j in range(0, total_length, word_length)]
            if Counter(words_in_substring) == word_count:
                result.append(i)
        
        return result

# Example usage
solution = Solution()
print(solution.findSubstring("barfoothefoobarman", ["foo", "bar"]))  
print(solution.findSubstring("wordgoodgoodgoodbestword", ["word", "good", "best", "word"]))  
print(solution.findSubstring("barfoofoobarthefoobarman", ["bar", "foo", "the"]))  
