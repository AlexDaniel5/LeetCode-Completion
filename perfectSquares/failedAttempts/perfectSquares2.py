class Solution(object):
    def numSquares(self, n):
        # A list of answers for every possible n value
        answers = [n] * (n + 1)
        # Set the base case
        answers[0] = 0
        # Loop for every answer possible and square possible
        for target in range(1, n + 1):
            for x in range(1, target + 1):
                square = x * x
                # If the current square is larger than the target break the loop
                if target - square < 0:
                    break
                # Update the number of perfect squares needed for the current target
                # Choose the minimum between the current value and the value obtained
                # by considering the current perfect square in the sum
                answers[target] = min(answers[target], 1 + answers[target - square])
        return answers[n]

solution = Solution()
solution.numSquares(12)