class Solution(object):
    def reverse(self, x):
        # Keep memory of if the input is negative and set x to a positive integer; easier to not deal with the negative sign
        sign = 1
        if x < 0:
            x = -x
            sign = -1
        # Convert the integer to a string to reverse its digits
        x_str = str(x)
        reversed_str = x_str[::-1]

        # Convert the reversed string back to an integer
        reversed_int = int(reversed_str)

        if sign == -1:
            reversed_int *= -1
        # Check if the integer fits within 32 bits
        if reversed_int < -2**31 or reversed_int > 2**31 -1:
            return 0
        return reversed_int

# To test the program
solution = Solution()
print(solution.reverse(-123))       # Output: -321
print(solution.reverse(1534236469)) # Output: 0