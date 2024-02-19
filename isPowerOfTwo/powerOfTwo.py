class Solution(object):
    def isPowerOfTwo(self, n):
        # All negative numbers aren't a power of two
        if n < 1:
            return False
        i = 0
        num = 0
        # Iterate until the signed integer maximum
        while num < 2147483648:
            num = 2 ** i
            if num == n:
                return True
            i += 1
        return False        