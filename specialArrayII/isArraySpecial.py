class Solution(object):
    def isArraySpecial(self, nums, queries):
        pref, cnt = [0], 0
        for i in range(1, len(nums)):
            # Check if the sum of the pair is odd, indicating parity
            if (nums[i - 1] + nums[i]) % 2 == 1:
                cnt += 1
            # Append the cumulative count of alternating pairs to pref
            pref.append(cnt)
        res = []
        for a, b in queries:
            # Check if the difference in the prefix sum matches the index range
            res.append(pref[b] - pref[a] == b - a)
        return res