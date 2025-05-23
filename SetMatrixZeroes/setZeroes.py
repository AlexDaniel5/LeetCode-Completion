class Solution(object):
    def setZeroes(self, matrix):
        m, n = len(matrix), len(matrix[0])
        # Boolean for if the first row or column has a zero
        firstRowZero = any(matrix[0][j] == 0 for j in range(n))
        firstColZero = any(matrix[i][0] == 0 for i in range(m))

        # Use the first row and column as markers
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Zero out cells based on markers
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # Zero out first row or column if needed
        if firstRowZero:
            for j in range(n):
                matrix[0][j] = 0
        if firstColZero:
            for i in range(m):
                matrix[i][0] = 0
        return matrix

print(Solution().setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]])) # [[0,0,0,0],[0,4,5,0],[0,3,1,0]]