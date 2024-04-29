class Solution(object):
    def longestCommonPrefix(self, strs):
        # Special cases
        if len(strs) == 1 or strs[0] == "":
            return strs[0]
        
        length = len(strs)
        wordLen = len(min(strs))
        prefix = ""
        i = 1 # Skip the first word
        j = 0
        # Iterate until we've reached the minimum word length
        while j < wordLen:
            char = strs[0][j]
            # Check if the character matches for the current index
            while i < length:
                if j == wordLen or strs[i][j] != char:
                    return prefix
                i += 1
            prefix += strs[0][j]
            i = 1
            j += 1
        return prefix
    
print(Solution().longestCommonPrefix(["flower","flow","flight"])) # fl