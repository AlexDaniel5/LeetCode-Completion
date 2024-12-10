from collections import defaultdict

class Solution(object):
    def maximumLength(self, s):
        sLen = len(s)
        substringLen = sLen - 2 # Subtract two to give at least three iterations in first loop
        substrings = defaultdict(int)
        # Loop for every length of substring starting at the highest
        while substringLen > 0:
            for i in range(sLen - substringLen + 1):
                substr = s[i:i + substringLen]
                # If all characters match
                if len(set(substr)) == 1:
                    substrings[substr] += 1
            # If we have a count of three, return it
            if any(value >= 3 for value in substrings.values()):
                return substringLen
            substrings.clear()
            substringLen -= 1
        return -1
    
print(Solution().maximumLength("aaaa")) # 2

