class Solution(object):
    def findDuplicate(self, nums):
        numCount = {}
        # Count the occurrences of each number
        for num in nums:
            numCount[num] = numCount.get(num, 0) + 1
        # Determine which number appeared twice
        for num, count in numCount.items():
            if count > 1:
                return num

print(Solution().findDuplicate([1,3,4,2,2])) # 2