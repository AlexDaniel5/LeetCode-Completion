class Solution(object):
    def divideArray(self, nums, k):
        nums.sort()
        output = self.divideArrays(nums)
        for array in output:
            if abs(array[0] - array[1]) > k or abs(array[0] - array[2]) > k or abs(array[1] - array [2]) > k:
                    return []
        return output

    def divideArrays(self, arr):
        numArrays = len(arr) // 3
        dividedArrays = [arr[i * 3: (i + 1) * 3] for i in range(numArrays)]
        return dividedArrays