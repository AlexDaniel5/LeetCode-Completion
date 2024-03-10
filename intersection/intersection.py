class Solution(object):
    def intersection(self, nums1, nums2):
        seen = set(nums1) # Create hashmap to perform lookups in constant time
        intersect = []
        for n in nums2:
            if n in seen:
                intersect.append(n)
                seen.remove(n) # Avoid duplicates
        return intersect
    
print(Solution().intersection([4,9,5], [9,4,9,8,4])) # [4,9] OR [9,4]