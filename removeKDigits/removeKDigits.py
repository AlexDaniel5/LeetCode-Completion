class Solution(object):
    def removeKdigits(self, num, k):
        stack = []
        for digit in num:
            print(stack)
            # If the element before the current digit is greater than pop it from the final
            while k > 0 and stack and stack[-1] > digit:
                k -= 1
                stack.pop()
            stack.append(digit)
        # If all the numbers are in increasing order and k > 0, remove the last k digits
        stack = stack[:len(stack) - k]
        result = "".join(stack) # Convert array to string
        i = 0
        # Remove any zeros at the beginning of the string
        while i < len(result) and result[i] == "0":
            i += 1
        result = result[i:]
        # Ensure we don't return an empty string
        if result:
            return result
        return "0"
    
print(Solution().removeKdigits("5337", 2)) # 33
print(Solution().removeKdigits("10001", 4)) # 0
print(Solution().removeKdigits("1432219", 3)) # 1219
print(Solution().removeKdigits("987654321", 3)) # 654321
print(Solution().removeKdigits("123456789", 3)) # 123456