class Solution:
    def findOrder(self, numCourses, prerequisites):
        adj = [[] for _ in range(numCourses)]

        for course, pre in prerequisites:
            adj[course].append(pre)

        visited = set()     # Current recursion stack
        done = set()        # Already processed
        order = []

        def dfs(course):
            if course in visited:
                return False      # Cycle found

            if course in done:
                return True

            visited.add(course)

            for pre in adj[course]:
                if not dfs(pre):
                    return False

            visited.remove(course)
            done.add(course)
            order.append(course)

            return True

        for course in range(numCourses):
            if not dfs(course):
                return []

        return order