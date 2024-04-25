class Solution(object):
    def longestIdealString(self, s, k):
        dp = [0] * 26
        for char in s:
            # Finds the numeric value of the character
            curr = ord(char) - ord("a")
            print("Current",char)
            longest = 1
            for prev in range(26):
                # Update longest
                if abs(curr - prev) <= k:
                    longest = max(longest, 1 + dp[prev])
            print("End Result",longest, dp[curr])
            # Update the current value of the character
            dp[curr] = max(dp[curr], longest)
        return max(dp)
    
print(Solution().longestIdealString("dyyonfvzsretqxucmavxegvlnnjubqnwrhwikmnnrpzdovjxqdsatwzpdjdsneyqvtvorlwbkb", 7)) # 42