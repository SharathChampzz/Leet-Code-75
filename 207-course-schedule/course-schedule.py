class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True

        graph = defaultdict(list)
    
        # build graph
        for src, dest in prerequisites:
            graph[src].append(dest)

        for i, j in graph.items():
            print(f'{i} => {j}')

        visited = [0] * numCourses # 0 - Not Visited, 1 - Visiting, 2 - Visited 

        def check_loop(current_course) -> bool:
            if visited[current_course] == 1:
                return False # node is currenly marked visiting, and we are back again to the same node

            if visited[current_course] == 2:
                return True # this node or course can be successfully completed as per previous analysis

            visited[current_course] = 1 # we are currently visiting this

            for next_course in graph[current_course]:
                status = check_loop(next_course)
                if not status:
                    return False
            
            visited[current_course] = 2 # we completed visiting this, no loop

            return True

        for course_id in range(numCourses):
            if not check_loop(course_id):
                return False

        return True
