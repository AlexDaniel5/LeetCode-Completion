class Solution(object):
    def majorityElement(self, nums):
        numbersCount = {}
        # Get a count of every number
        for number in nums:
            if number in numbersCount:
                numbersCount[number] += 1
            else:
                numbersCount[number] = 1
        highestCount = -1
        highestNum = None
        # Check which number has the highest count
        for number, count in numbersCount.items():
            if highestCount < count:
                highestCount = count
                highestNum = number
        return highestNum
    
nums = [2,2,1,1,2]
solution = Solution()
print(solution.majorityElement(nums))