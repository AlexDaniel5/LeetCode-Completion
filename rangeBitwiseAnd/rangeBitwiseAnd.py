class Solution(object):
    def rangeBitwiseAnd(self, left, right):
        count = 0
        print("started", left, right, count)
        while left != right:
            left >>= 1
            right >>= 1
            count += 1
            print(left, right, count)
        print("ended", left, right, count)
        return left << count

solution = Solution()
print("answer",solution.rangeBitwiseAnd(5, 7)) # 4
print("answer",solution.rangeBitwiseAnd(1, 2147483647)) # 0
print("answer",solution.rangeBitwiseAnd(1, 2)) # 0
print("answer",solution.rangeBitwiseAnd(2, 5)) # 0
print("answer",solution.rangeBitwiseAnd(3, 4)) # 0