from collections import deque

class Solution(object):
    def shortestDistanceAfterQueries(self, n, queries):
        def shortestPath():
            queue = deque()
            queue.append((0, 0)) # Start BFS from node 0 with distance 0
            visited = set()
            visited.add(0) # Mark node 0 as visited
            while queue:
                cur, length = queue.popleft()
                # Check if the destination node is reached
                if cur == n - 1:
                    return length
                # Explore neighbors of the current node
                for neighbour in adj[cur]:
                    if neighbour not in visited:
                        queue.append((neighbour, length + 1)) # Add neighbor with updated distance
                        visited.add(neighbour)

        # Initialize adjacency list with default edges (0 to n - 1)
        adj = [[i + 1] for i in range(n)]
        res = []
        for src, dst in queries:
            adj[src].append(dst) # Add shortcut from src to dst
            res.append(shortestPath()) # Calculate shortest path after each query
        return res
    
print(Solution().shortestDistanceAfterQueries(4, [[0,3],[0,2]])) # [1,1]
