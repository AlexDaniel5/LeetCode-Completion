class Solution(object):
    def reverse(self, x):
        # Convert the integer to a string to reverse its digits
        x_str = str(x)
        reversed_str = x_str[::-1]
        # If the reversed string has a negative sign at the end rewrite the string to have it at the front
        if reversed_str[-1] == '-':
            reversed_str = '-' + reversed_str[:-1]
        reversed_int = int(reversed_str)

        # Check if the integer fits within 32 bits
        if reversed_int < -2**31 or reversed_int > 2**31 -1:
            return 0
        return reversed_int

# To test the program
solution = Solution()
print(solution.reverse(-123))       # Output: -321
print(solution.reverse(1534236469)) # Output: 0