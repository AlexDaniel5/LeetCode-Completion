class Solution(object):
    def findDuplicates(self, nums):
        duplicates = set() # Faster search time than an array
        result = []
        for num in nums:
            # Found duplicate
            if num in duplicates:
                result.append(num)
            # First occurence of the number
            else:
                duplicates.add(num)
        return result