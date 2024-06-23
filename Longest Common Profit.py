class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs is None: return None
        result = strs[0]
        for word in strs[1:]:
            i = 0
            while i < len(word) and i < len(result):
                if word[i] != result[i]:
                    result = result[0:i:]
                    break
                i += 1
            else: result = result[:i]
        return result
