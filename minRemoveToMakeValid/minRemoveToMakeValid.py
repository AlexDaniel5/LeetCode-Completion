class Solution(object):
    def minRemoveToMakeValid(self, s):
        stack = []
        result = []
        for char in s:
            # Append the index of where the front parantheses would be in the result string
            if char == "(":
                stack.append(len(result))
            # If we have exisiting front parantheses in the stack pop it's index so it won't get removed in the final string
            elif char == ")":
                if stack:
                    stack.pop()
                # Else don't add it to the result string
                else:
                    continue
            result.append(char)
        # For any front parantheses that don't have a matching back parantheses will be removed
        for index in stack:
            result[index] = ""
        return "".join(result) # Convert the array back to a string
    
print(Solution().minRemoveToMakeValid("a)b(c)d")) # ab(c)d
print(Solution().minRemoveToMakeValid("lee(t(((c)o)de)")) # leet(((c)o)de)