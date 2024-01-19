class Solution(object):
    def minFallingPathSum(self, matrix):
        rows, cols = len(matrix), len(matrix[0])

        # Initialize the result matrix with dimensions (rows + 1) x (cols + 1)
        result = [[float("inf")] * (cols + 1) for i in range (rows + 1)]
        
        # Set the bottom-right element to 0, representing the base case for the last row
        result[rows - 1][cols] = 0
        
        # Dynamic Programming Loop
        for i in range (rows - 1, -1, -1):
            for k in range (cols - 1, -1, -1):
                # Update the result matrix with the minimum falling path sum
                result[i][k] = matrix[i][k] + min(result[i + 1][k], result[i][k + 1])

        # Return the minimum falling path sum starting from the top-left corner
        return result[0][0]
    
# To Test Code
matrix1 = [[2, 1, 3], [6, 5, 4], [7, 8, 9]]
matrix2 = [[-19, 57], [-40, -5]]
sol = Solution()

result1 = sol.minFallingPathSum(matrix1)
result2 = sol.minFallingPathSum(matrix2)
print("Test Case 1:")
print("Input Matrix:")
for row in matrix1:
    print(row)
print("Output:", result1)
print()

print("Test Case 2:")
print("Input Matrix:")
for row in matrix2:
    print(row)
print("Output:", result2)