class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m, n = len(maze), len(maze[0])

        def bfs(start_node: Tuple[int, int]) -> int:
            queue = deque([(start_node, 0)])  # Queue for BFS, storing (node, step_count)
            visited = set()
            visited.add(start_node)

            while queue:
                (x, y), step_count = queue.popleft()
                print(f'Now exploring: {(x, y)} with step count: {step_count}')

                # Possible moves: down, right, up, left
                possible_moves = [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]

                for nx, ny in possible_moves:
                    if 0 <= nx < m and 0 <= ny < n and maze[nx][ny] == '.' and (nx, ny) not in visited:
                        print(f'Adding {(nx, ny)} to visited...')
                        queue.append(((nx, ny), step_count + 1))
                        visited.add((nx, ny))

                        # Check if the current node is an exit (not the entrance)
                        if (nx == 0 or ny == 0 or nx == m - 1 or ny == n - 1) and (nx, ny) != tuple(entrance):
                            return step_count + 1

            return -1  # Return -1 if no exit is found

        result = bfs(tuple(entrance))
        return result
