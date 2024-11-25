class Solution(object):
    def rotateTheBox(self, box):
        length = len(box[0])
        for row in box:
            rp = length - 1
            for lp in reversed(range(length)):
                # Relocate where stones will fall
                if row[lp] == "*":
                    rp = lp - 1
                elif row[lp] == "#":
                    # Don't swap if the pointers are in the same location
                    if lp != rp:
                        row[rp], row[lp] = row[lp], row[rp]
                    rp -= 1
        # Rotates matrix 90 degrees clockwise
        return list(map(list, zip(*reversed(box))))
    
print(Solution().rotateTheBox([["#","#","#","#","#"],["#","#","#","#","#"],["#","#","#","#","#"],["#","#","#","#","#"],["#","#","#","#","#"]]))
# [["#","#","#","#","#"],["#","#","#","#","#"],["#","#","#","#","#"],["#","#","#","#","#"],["#","#","#","#","#"]]