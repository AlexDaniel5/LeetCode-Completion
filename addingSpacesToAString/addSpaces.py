class Solution(object):
    def addSpaces(self, s, spaces):
        newStr = []
        spaceLen, sLen = len(spaces), len(s)
        i, j = 0, 0
        while j < spaceLen:
            # Add a space
            if i == spaces[j]:
                newStr.append(" ")
                j += 1
            # Add a character
            newStr.append(s[i])
            i += 1
        # If we added all the sapces required, add the remaining of the string
        if i < sLen:
            newStr.append(s[i:])
        # Convert from a list to a string
        return "".join(newStr)
    
print(Solution().addSpaces("spacing", [0,1,2,3,4,5,6])) # " s p a c i n g"