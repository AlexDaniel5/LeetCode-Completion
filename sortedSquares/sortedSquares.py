class Solution(object):
    def sortedSquares(self, nums):
        return sorted(i*i for i in nums)

solution = Solution()
print(solution.sortedSquares([-7, -3, 2, 3, 11])) # [4,9,9,49,121]