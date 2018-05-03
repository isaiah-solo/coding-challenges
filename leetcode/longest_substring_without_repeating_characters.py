# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        result = ""
        current = ""
        
        for char in s:
            if char not in current:
                current += char
                continue
                
            if len(current) > len(result):
                result = current
                
            current = current[current.index(char) + 1 :]
            current += char
        
        result = current if len(current) > len(result) else result
        
        return len(result)
