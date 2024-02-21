class Solution(object):
    def rangeBitwiseAnd(self, left, right):
        if left == right:
            return left
        msb = 1
        count = 0
        while left >= msb:
            msb *= 2
            count += 1
            print(count, msb)
        msb //= 2
        bitNum = 1
        result = 0
        diff = right - left
        print("The msb is", msb, "and the count is", count,"the difference is", diff)
        while msb >= bitNum:
            print(bitNum, end=" ")
            if diff < bitNum:
                print("yes")
                result += bitNum
            else:
                print("no")
            bitNum *= 2
        return result

solution = Solution()
print("answer",solution.rangeBitwiseAnd(5, 7)) # 4
print("answer",solution.rangeBitwiseAnd(1, 2147483647)) # 0
print("answer",solution.rangeBitwiseAnd(1, 2)) # 0
print("answer",solution.rangeBitwiseAnd(2, 5)) # 0
print("answer",solution.rangeBitwiseAnd(3, 4)) # 0 I get 2