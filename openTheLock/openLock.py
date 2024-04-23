from collections import deque

class Solution(object):
    def openLock(self, deadends, target):
        # The math to determine the next possible turn
        def children(lock):
            result = []
            for i in range(4):
                # Emulate adding one
                digit = str((int(lock[i]) + 1) % 10)
                result.append(lock[:i] + digit + lock[i+1:])
                # Emulate subtracting one
                digit = str((int(lock[i]) - 1 + 10) % 10)
                result.append(lock[:i] + digit + lock[i+1:])
            return result
        
        # Special case
        if "0000" in deadends:
            return -1
        queue = deque()   
        # Queue will be a set consisting of lock and turns  
        queue.append(["0000", 0])
        visited = set(deadends) # Initalize visited with the deadends

        while queue:
            lock, turns = queue.popleft()
            # If the combination is found
            if lock == target:
                return turns
            # For the 8 possibilities in each combination
            for child in children(lock):
                if child not in visited:
                    queue.append([child, turns+1])
                    visited.add(child)
        return -1