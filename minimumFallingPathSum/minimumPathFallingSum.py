class Solution(object):
    def minFallingPathSum(self, matrix):
        n = len(matrix)
        # Iterate through the matrix in a bottom-up manner 
        for i in reversed(range(n-1)): 
            for j in range(n):
                # Calculate values for the three possible choices in the row below
                # If the current element is in the leftmost column, set 'left' to a large value to handle the boundary condition
                left = 9999999 if j == 0 else matrix[i+1][j-1]
                right = 9999999 if j == n-1 else matrix[i+1][j+1]
                # Value directly below
                down = matrix[i+1][j]
                # Update the current element by adding the minimum of the three choices
                matrix[i][j] += min(left, down, right)
        # Return the minimum value in the first row of the modified matrix
        return min(matrix[0])
    
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