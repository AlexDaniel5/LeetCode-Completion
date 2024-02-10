class Solution(object):
    def myAtoi(self, s):
        # Rare case management
        if s == "":
            return 0
        if s[-1] == '-':
            s = s[:-1]
        string = ''
        negative = False
        numberHit = False
        signChange = False
        for char in s:
            # First if statement is to skip the character if it's a space
            if char == ' ':
                # However, if we already read a number skip it
                if numberHit or signChange:
                    break
            elif char == '-':
                # If we already finished reading a number
                if numberHit:
                     break
                # If we're dealing with multiple signs
                elif signChange:
                    return 0
                negative = True
                signChange = True
            elif char == '+':
                if numberHit:
                     break
                elif signChange:
                    return 0
                signChange = True
            # If we have characters after a number end the loop
            elif not char.isdigit() and numberHit:
                break
            # Start the number
            elif char.isdigit():
                string = string + char
                numberHit = True
            # If we have characters before the number
            elif not char.isdigit() and not numberHit:
                return 0
        # If we broke the loop with an empty string
        if len(string) < 1:
            return 0
        else:
            result = int(string)
        if negative:
            result *= -1
        # If we exceeded the max signed 32-bit integer
        if result > 2147483647:
            return 2147483647
        elif result < -2147483648:
            return -2147483648
        return result
    
solution = Solution()
print(solution.myAtoi("words and 987"))
print(solution.myAtoi("-91283472332"))
print(solution.myAtoi("3.14159"))
print(solution.myAtoi("   +0 123"))