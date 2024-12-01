class Solution(object):
    def checkIfExist(self, arr):
        nums = set()
        for num in arr:
            if num in nums:
                return True
            nums.add(num * 2)
            if num % 2 == 0:
                nums.add(num / 2)
        return False
    
print(Solution().checkIfExist([-2,0,10,-19,4,6,-8])) # False