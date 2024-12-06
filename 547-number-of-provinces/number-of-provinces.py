class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()  # Set to store visited nodes (cities)

        m, n = len(isConnected), len(isConnected[0])  # Number of cities (m == n)

        def dfs(i: int):
            if i in visited:
                return

            visited.add(i)  # Mark the current city as visited

            for j in range(n):
                if isConnected[i][j] == 1:  # If there is a direct connection
                    dfs(j)  # Recursively visit the connected city

        count = 0  # Counter for the number of provinces

        for i in range(m):
            if i not in visited:
                dfs(i)  # Start a DFS from the unvisited city
                count += 1  # Increment the province count

        return count
