class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set() # stores i

        m, n = len(isConnected), len(isConnected[0])

        def dfs(i):
            if i in visited:
                return

            visited.add(i)

            for j in range(n):
                if isConnected[i][j] == 1:
                    dfs(j)
           

        count = 0 # connected provinces count

        for i in range(m):
            if i not in visited:
                dfs(i)
                count += 1
            
        return count
