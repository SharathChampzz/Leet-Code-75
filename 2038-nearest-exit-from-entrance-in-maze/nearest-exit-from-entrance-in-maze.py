class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m = len(maze)
        n = len(maze[0])

        def bfs(start_node: tuple):
            queue = deque([[start_node, 0]])
            visited = set()
            visited.add(tuple(start_node))


            while queue:
                node = queue.popleft()
                x, y = node[0]
                step_count = node[1]
                print(f'Now exploring : {node}')

                possible_nodes = [(x+1, y), (x, y+1), (x-1, y), (x, y-1)]

                for node in possible_nodes:
                    node_x, node_y = node
                    if node_x >= 0 and node_y >= 0 and node_x < m and node_y < n and maze[node_x][node_y] == '.' and node not in visited:
                        print(f'Adding {node} to visited...')
                        queue.append([node, step_count + 1])
                        visited.add(node)

                        if node_x == 0 or node_y == 0 or node_x == m-1 or node_y == n-1:
                            return step_count + 1

            return -1

        result = bfs(tuple(entrance))

        print(result)

        return result





        