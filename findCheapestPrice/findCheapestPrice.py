import math

class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        prices = [float("inf")] * n
        prices[src] = 0

        # Iterate through each possible movement within the range of stops
        for i in range(k + 1):
            tmpPrices = prices[:]
            # Iterate through individual flight details (source, destination, price)
            for s, d, p in flights:
                # If it's impossible to reach the source node, skip to the next iteration
                if prices[s] == float("inf"):
                    continue
                # Update the temporary prices array if the price to reach the destination node is reduced
                if prices[s] + p < tmpPrices[d]:
                    tmpPrices[d] = prices[s] + p
            prices = tmpPrices
            
        # If it's impossible to reach the destination node, return -1; otherwise, return the cost
        if math.isinf(prices[dst]):
            return -1
        return prices[dst]
    
solution = Solution()
flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
print(solution.findCheapestPrice(4, flights, 0, 3, 1)) # 700