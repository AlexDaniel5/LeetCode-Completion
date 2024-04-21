from collections import defaultdict

class Solution(object):
    def validPath(self, n, edges, source, destination):
        def dfs(node, seen): 
            if node == destination:
                return True
            seen.add(node) # So, we don't run into infinite loops
            # Iterate through the dictionary and attempt to find th destination node
            for neighbor in adjList[node]:
                if neighbor not in seen:
                    if dfs(neighbor, seen):
                        return True
            return False
        
        seen = set()
        # Converting the list into a dictionary speeds up the algorithm
        adjList = defaultdict(list)
        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)
        return dfs(source, seen)
    
print(Solution().validPath(3, [[0,1],[1,2],[2,0]], 0, 2)) # True