class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        indegree = [0]*numCourses
        for u, v in prerequisites:
            graph[u].append(v)
        for i in range(numCourses):
            for adjacent in graph[i]:
                indegree[adjacent] += 1
        queue = [i for i, num in enumerate(indegree) if num==0]
        result = []

        while queue:
            node = queue.pop(0)
            result.append(node)
            for adjacent in graph[node]:
                indegree[adjacent] -= 1
                if indegree[adjacent]==0:
                    queue.append(adjacent)
        if len(result) == numCourses:
            return True
        else:
            return False
        #Using DFS
        graph = [[] for _ in range(numCourses)]
        for course, prerq in prerequisites:
            graph[prerq].append(course)
        visited = [0] *numCourses
        def hasCycle(course):
            if visited[course] == 1:
                return False
            if visited[course] == -1:
                return True
            visited[course] = -1
            for neighbor in graph[course]:
                if hasCycle(neighbor):
                    return True
            visited[course] = 1
            return False
        for course in range(numCourses):
            if hasCycle(course):
                return False
        return True
        
        #Using BFS
        graph = [[] for _ in range(numCourses)]
        in_degree = [0]*(numCourses)
        for course, prerq in prerequisites:
            graph[prerq].append(course)
            in_degree[course] += 1
        queue = deque([course for course in range(numCourses) if in_degree[course]== 0])
        count = 0
        while queue:
            course = queue.popleft()
            count += 1
            for neighbor in graph[course]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        return count == numCourses
        