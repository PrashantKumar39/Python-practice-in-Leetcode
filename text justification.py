lass Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res, curr, num_of_letters = [], [], 0

        for word in words:
            if num_of_letters + len(word) + len(curr) > maxWidth:
                for i in range(maxWidth - num_of_letters):
                    curr[i % (len(curr) - 1 or 1)] += ' '
                res.append(''.join(curr))
                curr, num_of_letters = [], 0
            curr += [word]
            num_of_letters += len(word)

        return res + [' '.join(curr).ljust(maxWidth)]

# Example usage
solution = Solution()
print(solution.fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16))
print(solution.fullJustify(["What","must","be","acknowledgment","shall","be"], 16))
print(solution.fullJustify(["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], 20))
