class Solution(object):
    def firstUniqChar(self, s):
        charCount = {}
        uniqueChars = []
        # Count the occurences of each character
        for char in s:
            charCount[char] = charCount.get(char, 0) + 1
        # Identify unique characters
        for key, value in charCount.items():
            if value == 1:
                uniqueChars.append(key)
        # Run through the input string and determine the first character with a character count of one
        for index, char in enumerate(s):
            if charCount[char] == 1:
                return index
        # If there are none one count characters
        return -1
    
# Test Example 1
solution_instance = Solution()
input_str = "leetcode"
print(solution_instance.firstUniqChar(input_str))
