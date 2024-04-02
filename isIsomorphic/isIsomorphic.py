class Solution(object):
    def isIsomorphic(self, s, t):
        mappedLetters = {}
        mappedValues = set()
        for i in range(len(s)):
            # If the letter is already mapped and the mapped value doesn't equal t[i] return False
            if s[i] in mappedLetters:
                if mappedLetters[s[i]] != t[i]:
                    return False
            else:
                # If a letter has already been mapped to that letter return False
                if t[i] in mappedValues:
                    return False
                # Map the letter of s to t
                mappedLetters[s[i]] = t[i]
                mappedValues.add(t[i])
        return True

print(Solution().isIsomorphic("badc", "baba")) # False
print(Solution().isIsomorphic("egg", "add")) # True