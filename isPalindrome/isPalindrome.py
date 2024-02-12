class Solution(object):
    def isPalindrome(self, x):
        # Negative numbers are always a false case
        if x < 0:
            return False
        # Special case: 0 is a palindrome
        if x == 0:
            return True
        numStr = str(x)
        # If the input number ends with 0, return false
        if numStr[-1] == '0':
            return False
        # Flip the integer as a string; so we can iterate through it
        numStr = numStr[::-1]
        # Convert the string back to an integer
        num = int(numStr)
        # Check if the numbers are equal
        if num == x:
            return True
        return False
    
solution = Solution()
print(solution.isPalindrome(123))
print(solution.isPalindrome(10))