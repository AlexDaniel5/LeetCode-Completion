class Solution(object):
    def maximumBeauty(self, nums, k):
        nums.sort()
        lenNums = len(nums)
        result = 0
        lp = 0
        for rp in range(lenNums):
            # Check if the difference exceeds k * 2
            while nums[rp] - nums[lp] > k * 2:
                lp += 1
            result = max(result, rp - lp + 1)
        return result

print(Solution().maximumBeauty([5,57,46], 15)) # 2