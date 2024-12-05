class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)

        def bfs():
            queue = deque([0])
            visited = set()
            visited.add(0) # visisted room 0

            while queue:
                room_index = queue.popleft()

                for key in rooms[room_index]:
                    if key not in visited:
                        visited.add(key)
                        queue.append(key)

            return len(visited) == len(rooms)

        return bfs()


        