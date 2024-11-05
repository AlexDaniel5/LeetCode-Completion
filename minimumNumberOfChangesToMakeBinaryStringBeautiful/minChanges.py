class Solution(object):
    def minChanges(self, s):
        result = 0
        # Iterate for every other character
        for i in range(0, len(s), 2):
            # Check if the current character matches the next character
            if s[i] != s[i + 1]:
                result += 1
        return result
    
print(Solution().minChanges("100010000111")) # 3