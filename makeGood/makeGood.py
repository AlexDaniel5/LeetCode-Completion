class Solution(object):
    def makeGood(self, s):
        stack = []
        i = 0
        while i < len(s):
            if (stack and # Stack isn't empty
                stack[-1] != s[i] and # Characters aren't the same lowercase letters
                stack[-1].lower() == s[i].lower()): # Characters equal eachother after put to lowercase
                stack.pop()
            else:
                stack.append(s[i])
            i += 1
        return "".join(stack) # Join every element in stack and convert it to a string
    
print(Solution().makeGood("abBAcC")) # ""
print(Solution().makeGood("leEeetcode")) # leetcode
