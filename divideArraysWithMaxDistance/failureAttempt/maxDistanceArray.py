class Solution(object):
    def divideArray(self, nums, k):
        sortedList = self.quicksort(nums)
        print(sortedList)
        output = self.divideArrays(sortedList)
        for array in output:
            # Check if any two elements in the array are larger than k
            if abs(array[0] - array[1]) > k or abs(array[0] - array[2]) > k or abs(array[1] - array [2]) > k:
                    return []
        return output

    def quicksort(self, arr): 
        if len(arr) <= 1:
            return arr
        else:
            pivot = arr[0]
            less = [x for x in arr[1:] if x <= pivot]
            greater = [x for x in arr[1:] if x > pivot]
            return self.quicksort(less) + [pivot] + self.quicksort(greater)

    def divideArrays(self, arr):
        # Calculate the number of arrays
        numArrays = len(arr) // 3
        # Create arrays, each with 3 elements
        # [arr[i * 3: (i + 1) * 3] tells each subarray should be 3 elements
        # Ex. if i = 2, then start at index 6 and end at index 9
        dividedArrays = [arr[i * 3: (i + 1) * 3] for i in range(numArrays)]
        return dividedArrays

# To test
solution_instance = Solution()
nums = [5, 3, 8, 1, 2, 7, 4, 6]
k = 3
result = solution_instance.divideArray(nums, k)