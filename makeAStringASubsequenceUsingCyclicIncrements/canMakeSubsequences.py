class Solution(object):
    def canMakeSubsequence(self, str1, str2):
        i, j = 0, 0
        # A dictionary mapping each letter to the next letter
        nextLetter = {
            'a': 'b', 'b': 'c', 'c': 'd', 'd': 'e', 'e': 'f', 
            'f': 'g', 'g': 'h', 'h': 'i', 'i': 'j', 'j': 'k', 
            'k': 'l', 'l': 'm', 'm': 'n', 'n': 'o', 'o': 'p', 
            'p': 'q', 'q': 'r', 'r': 's', 's': 't', 't': 'u', 
            'u': 'v', 'v': 'w', 'w': 'x', 'x': 'y', 'y': 'z', 'z': 'a'
        }
        lenStr1, lenStr2 = len(str1), len(str2)
        while i < lenStr1 and j < lenStr2:
            # If we have a character match for the two pointers
            if str1[i] == str2[j] or nextLetter[str1[i]] == str2[j]:
                j += 1
            i += 1
        # If the second pointer made it through all of the second string, return True
        return j == lenStr2

print(Solution().canMakeSubsequence("zc", "ad")) # True
print(Solution().canMakeSubsequence("ab", "d")) # False