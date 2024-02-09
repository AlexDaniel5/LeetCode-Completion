class Solution(object):
    def numSquares(self, n):
        perfectSquares = []
        for number in range(1, n + 1):
            squareRoot = int(number ** 0.5)
            if squareRoot ** 2 == number:
                perfectSquares.append(number)
        perfectSquares.reverse()
        count = 0
        x = 0
        for number in perfectSquares:
            while x + number <= n:
                x += number
                count += 1
                print(number)
        return count