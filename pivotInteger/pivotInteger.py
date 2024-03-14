class Solution(object):
    def pivotInteger(self, n):
        # Find the total sum of n
        rightSum = sum(range(n + 1))
        leftSum = 0
        # Increase the pivot integer and decrease the total sum
        for i in range(1, n + 1):
            leftSum += i
            print(leftSum, rightSum, i)
            if leftSum == rightSum:
                return i
            rightSum -= i
        return -1 # No pivot integer found

print(Solution().pivotInteger(8)) # 6
print(Solution().pivotInteger(1)) # 1
print(Solution().pivotInteger(4)) # -1