import functools

class Solution(object):
    def largestNumber(self, nums):
        # Convert numbers to strings for easier comparison
        nums = [str(num) for num in nums]

        # Compare concatenated strings to determine optimal order
        def compare(a, b):
            if a + b > b + a:
                return -1
            elif a + b < b + a:
                return 1
            else:
                return 0
        
        # Sort the array using the custom comparison function
        sortedNums = sorted(nums, key=functools.cmp_to_key(compare))
        # Handle edge case of all zeros (e.g., [0, 0])
        return str(int(''.join(sortedNums)))

print(Solution().largestNumber([3, 30, 34, 5, 9])) # "9534330"
print(Solution().largestNumber([0, 0])) # "0"