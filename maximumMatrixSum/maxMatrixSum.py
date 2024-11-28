class Solution(object):
    def maxMatrixSum(self, matrix):
        totalSum = 0
        negCount = 0
        minAbsVal = float('inf')
        for row in matrix:
            for cell in row:
                absVal = abs(cell) # Treat every number as positive
                totalSum += absVal
                minAbsVal = min(minAbsVal, absVal) # Find absolute smallest number
                if cell < 0:
                    negCount += 1
        # If the number of negatives is odd, consider the smallest absolute value as negative
        if negCount % 2 == 1:
            totalSum -= 2 * minAbsVal
        return totalSum
    
print(Solution().maxMatrixSum([[-1,0,-1],[-2,1,3],[3,2,2]])) # 15