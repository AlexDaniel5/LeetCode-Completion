class Solution(object):
    def minimizedMaximum(self, n, quantities):
        # Determine if each store can obtain at least k products
        def canDistribute(k):
            stores = 0
            for product in quantities:
                stores += (product + k - 1) / k # math.ceil() isn't working on LC; math.ceil(product/k)
                print(stores)
            return stores > n # When true, indicates every store got up to k products

        l, r = 1, max(quantities)
        result = 0
        # Binary search algorithm
        while l <= r:
            x = (l + r) // 2
            if canDistribute(x):
                l = x + 1
            else:
                result = x
                r = x - 1
        return result

print(Solution().minimizedMaximum(2, [5, 7])) # 7