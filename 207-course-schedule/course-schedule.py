from typing import List, Optional
from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Build the graph
        graph = defaultdict(list)
        for src, dest in prerequisites:
            graph[dest].append(src)

        # Visited states: 0 - Not Visited, 1 - Visiting, 2 - Visited
        visited = [0] * numCourses

        def check_loop(course: int) -> bool:
            if visited[course] == 1:
                return False  # Detected a cycle
            if visited[course] == 2:
                return True  # Already checked and no cycle

            visited[course] = 1  # Mark as visiting
            for next_course in graph[course]:
                if not check_loop(next_course):
                    return False

            visited[course] = 2  # Mark as visited
            return True

        # Check each course for cycles
        for course_id in range(numCourses):
            if not check_loop(course_id):
                return False

        return True
