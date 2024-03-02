class Solution(object):
    def maximumOddBinaryNumber(self, s):
        # Count the number of 1s in the input
        oneCount = 0
        digits = 0
        for i in s:
            if i == "1":
                oneCount += 1
            digits += 1

        # Convert the binary number into all 0s with the correct amount of digits
        output = "0" * digits
        # Special case: If there are no '1's in the original number, return the all 0s string
        if oneCount == 0:
            return output
        
        outputList = list(output)  # Convert to list for easy string manipulation
        # Set the last digit to 1 for oddness and set all the higher-order digits to 1 for the greatest value
        outputList[-1] = "1"
        for i in range(oneCount - 1):
            outputList[i] = "1"
        # Convert the list back to a string
        return ''.join(outputList)

solution = Solution()
print(solution.maximumOddBinaryNumber("0101")) # 1001