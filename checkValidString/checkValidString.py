class Solution(object):
    def checkValidString(self, s):
        pMin = 0
        pMax = 0
        for char in s:
            if char == "(":
                pMin += 1
                pMax += 1
            elif char == ")":
                pMin -= 1
                pMax -= 1
            # Must be asterisk
            else:
                pMin -= 1
                pMax += 1
            # Too many closing parentheses, must be false
            if pMax < 0:
                return False
            # Asterisk could've been an opening parantheses, don't let it go negative
            if pMin < 0:
                pMin = 0
        return pMin == 0
    
print(Solution().checkValidString("(*))")) # True
        