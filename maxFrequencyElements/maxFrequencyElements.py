class Solution(object):
    def maxFrequencyElements(self, nums):
        numCount = {}
        # Count the occurrences of each number
        for num in nums:
            numCount[num] = numCount.get(num, 0) + 1
        # Sort the hash table by its values
        sortedNumCount = sorted(numCount.items(), key=lambda x: x[1], reverse=True)
        # Identify the highest value count
        maxFrequency = sortedNumCount[0][1]
        i = 1
        count = maxFrequency
        # Add the value of each key with the same value count
        while i < len(sortedNumCount) and sortedNumCount [i][1] == maxFrequency:
            count += maxFrequency
            i += 1
        return count

print(Solution().maxFrequencyElements([1,2,2,3,1,4])) # 4