"""class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)] 
        for u,v in prerequisites: # u = index v = value
            adj[u] = v
        visited = set()
        def dfs(cur_course):
            if cur_course in visited:
                return False
            if adj[cur_course] == []:
                return True
            visited.add(cur_course)
            for cors in adj[cur_course]:
                if not dfs(cors):
                    return False
            adj[cur_course] = []
            visited.remove(cur_course)
            return True
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True"""

class Solution:
    def canFinish(self, numCourses,prerequisites) -> bool:
        # 1. Build the adjacency list correctly
        adj = [[] for _ in range(numCourses)]
        for course, pre in prerequisites:
            adj[course].append(pre)
        
        visited = set() # Tracks courses in the current DFS path (recursion stack)

        def dfs(cur_course):
            if cur_course in visited: # Cycle detected
                return False
            if adj[cur_course] == []: # No prerequisites, path is clear
                return True
            
            visited.add(cur_course)
            for pre in adj[cur_course]:
                if not dfs(pre):
                    return False
            
            # Backtrack and optimize: remove from path and clear adj to avoid re-scanning
            visited.remove(cur_course)
            adj[cur_course] = [] 
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        
        return True

"""class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        pre = defaultdict(list)

        for course, p in prerequisites:
            pre[course].append(p)
        
        taken = set()

        def dfs(course):
            if not pre[course]:
                return True
            
            if course in taken:
                return False
            
            taken.add(course)

            for p in pre[course]:
                if not dfs(p): return False
            
            pre[course] = []
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False

        return True"""