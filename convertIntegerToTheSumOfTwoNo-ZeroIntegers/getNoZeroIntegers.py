class Solution(object):
    def getNoZeroIntegers(self, n):
        a = 1
        b = n - 1
        while a < n:
            # Convert to string to check if the number contains 0s
            if "0" in str(a) or "0" in str(b):
                a += 1
                b -= 1
            else:
                return [a, b]
            
print(Solution().getNoZeroIntegers(11)) # [2, 9]