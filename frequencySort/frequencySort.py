class Solution(object):
    def frequencySort(self, s):
        charCount = {}
        # Get the character count of the string
        for char in s:
            charCount[char] = charCount.get(char, 0) + 1
        # Sorts the characters by count
        charCount = sorted(charCount.items(), key = lambda x: x[1], reverse = True)
        output = ""
        # Add the characters to the output string
        for char, count in charCount:
            output += char * count
        return output

solution = Solution()
str = "Aabb"
print(solution.frequencySort(str))