# https://leetcode.com/problems/string-to-integer-atoi/description/

class Solution:
        
    maxInt = 2147483648
    minInt = -2147483648
    
    def myAtoi(self, string):
        """
        :type str: str
        :rtype: int
        """
        
        # Separate string into tokens, and work only with first valid token
        tokens = string.split(' ')
        
        # Iterate through tokens
        for token in tokens:
            
            # Return 0 if invalid token
            if not token:
                continue
            
            # Assigning sign character if exists
            signChar = token[0] if token.startswith('+') or token.startswith('-') else None
            
            # Set sign based on sign character
            sign = -1 if signChar and signChar == '-' else 1
            
            # Update current token based on sign character
            token = token[1:] if signChar else token
            
            # Regex match for correct int/float format
            m = re.match(r'[0-9]+(\.[0-9]+)?', token)
            
            # Return 0 if no match
            if not m:
                break
            
            token = m.group(0)
            
            # Convert float to int if applicable
            token = token[:token.index('.')] if '.' in token else token
            
            # Factor in sign into value
            value = sign * int(token)
            
            # Alter value based on thresholds
            value = min(value, self.maxInt - 1)
            value = max(value, self.minInt)
            
            return value
        
        return 0
