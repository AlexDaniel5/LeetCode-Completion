class Solution(object):
    def minimumSteps(self, s):
        lp = 0
        total = 0
        for rp in range(len(s)):
            if s[rp] == "0":
                # Swap every black ball for the one white ball
                total += (rp - lp)
                lp += 1
        return total

print(Solution().minimumSteps("1001001")) # 6