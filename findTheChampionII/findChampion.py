class Solution(object):
    def findChampion(self, n, edges):
        team = [0] * n
        # Determine all weaker teams
        for src, dst in edges:
            team[dst] += 1
        champion = -1
        for i in range(n):
            # If a team has never been weaker
            if team[i] == 0:
                # Only one team can be the champion
                if champion != -1:
                    return -1
                champion = i
        return champion
    
print(Solution().findChampion(4, [[0,1],[2,0],[2,1]])) # -1
print(Solution().findChampion(3, [[0,1],[1,2]])) # 0