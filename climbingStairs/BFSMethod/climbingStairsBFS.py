# BFS is too slow! O(n^2)
class Solution(object):
    def climbStairs(self, n):
        queue = deque([0])
        ways = 0

        while queue:
            current_step = queue.popleft()

            # If we have reached the top, increment the ways
            if current_step == n:
                ways += 1

            # Otherwise, add possible next steps to the queue
            elif current_step < n:
                queue.append(current_step + 1)
                queue.append(current_step + 2)

        return ways
