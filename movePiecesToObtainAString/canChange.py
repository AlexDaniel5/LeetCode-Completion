class Solution(object):
    def canChange(self, start, target):
        i, j = 0, 0
        n = len(start)
        while i < n and j < n:
            # Two letters
            if start[i] != "_" and target[j] != "_":
                if target[j] == start[i]:
                    # Check if the letter can make it to the designated spot with movement requirements
                    if (target[j] == "R" and i <= j) or (target[j] == "L" and i >= j):
                        i += 1
                        j += 1
                    else:
                        return False
                # Not same letter
                else:
                    return False
            if i < n and start[i] == "_":
                i += 1
            if j < n and target[j] == "_":
                j += 1
        # If there are extra letters with no match, return False
        if (i < n and ("R" in start[i:] or "L" in start[i:])) or (j < n and ("R" in target[j:] or "L" in target[j:])):
            return False
        return True

print(Solution().canChange("_L__R__R_L", "L______RR_")) # True