class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        
        # as this is directed graph, we cannot reach all the nodes, to even check if we can fix the router
        # so build a bidirectional graph, that has the current direction set too.
        # If the current direction is outward, it means we need to reverse it. But we just count. So increment route count.

        graph = defaultdict(list) # adjancency list

        for a, b in connections:
            graph[a].append((b, False)) # outward
            graph[b].append((a, True)) # inward

        visited = set()
        def dfs(current_node):
            visited.add(current_node)
            count = 0

            for node, direction in graph[current_node]:
                if node not in visited:
                    if direction == False:
                        count += 1 # current route
                    count += dfs(node) # upcoming routes

            return count 

        result = dfs(0)

        return result

        
