class Solution(object):
    def getCommon(self, nums1, nums2):
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                return nums1[i]
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                i += 1
        return -1 # No matching numbers

print(Solution().getCommon([1,2,3],[2,4])) # 2