class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)

        def bfs(start_node):
            queue = deque([start_node])
            visited = set()
            visited.add(0) # visisted room 0

            while queue:
                room_index = queue.popleft()

                for key in rooms[room_index]:
                    if key not in visited:
                        visited.add(key)
                        queue.append(key)

            return len(visited) == len(rooms)

        visited = set()
        def dfs(current_room):
            visited.add(current_room)

            for key in rooms[current_room]:
                if key not in visited:
                    dfs(key)


        # return bfs(0)
        dfs(0)
        return len(visited) == len(rooms)


        