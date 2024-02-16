from collections import Counter

class Solution(object):
    def findLeastNumOfUniqueInts(self, arr, k):
        # Receive a count of all the numbers in the list
        numberCount = Counter(arr)
        # Organize the numbers in the list by their count and then by the number itself
        sortedNum = sorted(arr, key=lambda x: (numberCount[x], x))
        uniqueNumbers = set()
        ans = 0
        # Loop through the sorted list
        for num in sortedNum:
            # Exclude the first k numbers
            if k > 0:
                k -= 1
            # After excluding the first k numbers, count only unique numbers
            elif num not in uniqueNumbers:
                uniqueNumbers.add(num)
                ans += 1
        return ans
    
solution = Solution()
nums = [24,119,157,446,251,117,22,168,374,373,323,311,441,213,120,412,200,236,328,24,164,104,331,32,19,223,89,114,152,82,456,381,355,343,157,245,443,368,229,49,82,16,373,142,240,125,8]
print(solution.findLeastNumOfUniqueInts(nums, 41)) # 3