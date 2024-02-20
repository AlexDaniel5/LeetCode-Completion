class Solution(object):
    def missingNumber(self, nums):
        nums.sort()
        length = len(nums)
        for i in range(length):
            if i != nums[i]:
                return i
        return length # To get around the 'can't return None' syntax error