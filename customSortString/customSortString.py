class Solution(object):
    def customSortString(self, order, s):
        charCount = {}
        # Find the frequency of each chararcter in the string
        for char in s:
            charCount[char] = charCount.get(char, 0) + 1
        output = [] # List for easy string manipulation
        # Add each character that appears in order to the output
        for char in order:
            if char in charCount:
                output.append(char * charCount[char])
                del charCount[char] # Delete so we don't add in next loop
        # Add the rest of the characters, the order doesn't matter now
        for char, count in charCount.items():
            output.append(char * count)
        return "".join(output) # Convert list to string and return
    
print(Solution().customSortString("cba", "abcd")) # cbad