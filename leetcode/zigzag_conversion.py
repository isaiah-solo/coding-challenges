# https://leetcode.com/problems/zigzag-conversion/description/

class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        
        # Any input with strings less than 3 characters are the string itself,
        # no matter the number of rows
        if len(s) < 3:
            return s
        
        start = 0
        skips = []
        result = ""
        beginSpot = 0
        
        # Save the alternating skips for each row
        for num in range(numRows):
            skips.append([2 * (numRows - num - 1), 2 * num])
        
        # Grab the characters from each row
        for skip in skips:
            
            # Ititialize current starting spot
            currSpot = beginSpot
            beginSpot += 1
            
            # First and second skips
            first = skip[0]
            second = skip[1]
            
            # Use rest of string if skips are 0, to prevent endless loop
            if first == second and first == 0:
                result += s[currSpot:]
                continue
            
            # Switch to alternate first and second skips
            flag = True
    
            # Iterate through string using skips
            while currSpot < len(s):
                toSkip = first if flag else second
                
                # Append to result string
                result += s[currSpot] if toSkip > 0 else ""
                
                # Go to next spot in string
                currSpot += toSkip
                
                flag = not flag
        
        return result
