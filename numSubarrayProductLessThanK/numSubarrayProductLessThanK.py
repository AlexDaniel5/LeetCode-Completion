class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        subArrayCount = 0
        l = 0
        product = 1
        length = len(nums)
        for r in range(length):
            product *= nums[r]
            # While our product is greater than k decrease the left interval of our window
            while l <= r and product >= k:
                product = product // nums[l]
                l += 1
            subArrayCount += r - l + 1 # Formula for subarray count
        return subArrayCount

print(Solution().numSubarrayProductLessThanK([10,5,2,6], 100)) # 8