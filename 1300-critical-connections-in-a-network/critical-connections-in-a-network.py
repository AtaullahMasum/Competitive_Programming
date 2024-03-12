
class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        graph = [[]for _ in range(n)]
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)
        time = 0
        parent = [-1]*n
        disc = [-1]*n
        low = [-1]*n
        bridges = []
        def dfs(node):
            nonlocal time
            disc[node] = time
            low[node] = time
            time += 1
            for adjacent_node in graph[node]:
                if disc[adjacent_node] == -1:
                    parent[adjacent_node] = node
                    dfs(adjacent_node)
                    low[node] = min(low[node], low[adjacent_node])

                    if low[adjacent_node] > disc[node]:
                        bridges.append([node, adjacent_node])
                elif adjacent_node != parent[node]:
                    low[node] = min(low[node], disc[adjacent_node])
        for node in range(n):
            if disc[node] == -1:
                dfs(node)
        return bridges