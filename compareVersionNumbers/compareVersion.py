class Solution(object):
    def compareVersion(self, version1, version2):
        # Split the versions into segments
        v1 = version1.split(".")
        v2 = version2.split(".")
        # Calculate the number of segments
        l1 = len(v1)
        l2 = len(v2)

        # For every segment check which integer is larger
        for i in range(max(l1, l2)):
            # The last segment of version 1 has been passed, thus it must be 0
            if  i >= l1:
                n1 = 0
            # Convert the segment into an integer
            else:
                n1 = int(v1[i])

            if i >= l2:
                n2 = 0
            else:
                n2 = int(v2[i])
            # If the segments aren't equal return the result
            if n1 > n2:
                return 1
            elif n1 < n2:
                return -1
        return 0
    
print(Solution().compareVersion("1.01", "1.001")) # 0