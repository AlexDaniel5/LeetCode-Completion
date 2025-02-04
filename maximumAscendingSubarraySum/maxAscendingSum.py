class Solution(object):
    def maxAscendingSum(self, nums):
        prevNum = 0
        curSum = 0
        bestSum = 0
        for num in nums:
            # Descending
            if prevNum >= num:
                # Check for new best
                if bestSum < curSum:
                    bestSum = curSum
                curSum = 0 # Reset
            curSum += num
            prevNum = num
        return max(bestSum, curSum) # In case if the last sum is largest
    
print(Solution().maxAscendingSum([3,6,10,1,8,9,9,8,9])) # 19