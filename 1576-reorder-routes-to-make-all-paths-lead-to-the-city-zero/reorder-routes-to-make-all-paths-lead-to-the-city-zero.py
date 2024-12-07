class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        """
        This function determines the minimum number of edges that need to be reversed
        to make all paths lead to city 0 in a directed graph.
        """

        # Build a bidirectional graph with direction information.
        # If the direction is outward (from a to b), it means we need to reverse it.
        graph = defaultdict(list)  # Adjacency list

        for a, b in connections:
            graph[a].append((b, False))  # Outward edge
            graph[b].append((a, True))   # Inward edge

        visited = set()  # Set to keep track of visited nodes

        def dfs(current_node: int) -> int:
            """
            Depth-First Search (DFS) to count the number of edges that need to be reversed.
            """
            visited.add(current_node)
            count = 0

            for node, direction in graph[current_node]:
                if node not in visited:
                    if not direction:
                        count += 1  # Increment count for outward edge
                    count += dfs(node)  # Recursively visit the next node

            return count

        def bfs(current_node: int):
            queue = deque([current_node])
            visited.add(current_node)
            count = 0

            while queue:
                node = queue.popleft()

                for val, direction in graph[node]:
                    if val not in visited:
                        if direction == False:
                            count += 1
                        queue.append(val)
                        visited.add(val)

            return count

        # result = dfs(0)  # Start DFS from city 0
        result = bfs(0)  # Start BFS from city 0

        return result
