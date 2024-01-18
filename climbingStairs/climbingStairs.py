class Solution(object):
    def climbStairs(self, n):
        one, two = 1, 1

        # Emulates fibonnaci sequence
        for i in range (n - 1):
            temp = one
            one = one + two
            two = temp
        return one

# To test code
n = int(input("Enter the number of steps: "))
solution = Solution()
result = solution.climbStairs(n)
print(f"Number of distinct ways to climb {n} steps: {result}")