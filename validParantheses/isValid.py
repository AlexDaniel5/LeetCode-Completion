class Solution(object):
    def isValid(self, s):
        stack = []
        matchingBrackets = {"(": ")", "{": "}", "[": "]"}
        for char in s:
            # If the character is a key
            if char in matchingBrackets:
                stack.append(char)
            # Checks if the stack is empty or if the most recent opening bracket doesn't match the closing bracket
            elif not stack or matchingBrackets[stack.pop()] != char:
                return False
        # If there is opening characters remaining, return False
        return not stack        
    
print(Solution().isValid("[")) # False
print(Solution().isValid("(]")) # False
print(Solution().isValid("()[]{}")) # True