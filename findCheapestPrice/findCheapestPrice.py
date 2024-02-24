import math

class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        prices = [float("inf")] * n
        prices[src] = 0
        for i in range(k + 1):
            tmpPrices = prices[:]
            for s, d, p in flights:
                if prices[s] == float("inf"):
                    continue
                if prices[s] + p < tmpPrices[d]:
                    tmpPrices[d] = prices[s] + p
            prices = tmpPrices
        if math.isinf(prices[dst]):
            return -1
        return prices[dst]
    
solution = Solution()
flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
print(solution.findCheapestPrice(4, flights, 0, 3, 1)) # 700