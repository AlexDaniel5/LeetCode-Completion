class Solution(object):
    def tribonacci(self, n):
        tribNums = [0, 1, 1]
        # Base case
        if n < 3:
            return tribNums[n]
        for i in range(n-2):
            tribNums[0], tribNums[1], tribNums[2] = tribNums[1], tribNums[2], sum(tribNums)
        return tribNums[2]
    
print(Solution().tribonacci(25)) # 1389537