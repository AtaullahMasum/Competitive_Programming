
class Solution:
  def  __init__(self):
    self.time = 0
  def dfs(self, node, disc, low, parent,bridges, adj ):
    disc[node] = self.time
    low[node] = self.time
    self.time += 1
    for adjacent_node in adj[node]:
      if disc[adjacent_node] == -1:
        parent[adjacent_node] = node 
        self.dfs(adjacent_node,disc, low, parent,bridges, adj)
        low[node] = min(low[node], low[adjacent_node])
        if low[adjacent_node] > disc[node]:
          bridges.append((node, adjacent_node))
      elif adjacent_node != parent[node]: #if child to parent then ignore
        low[node] = min(low[node], disc[adjacent_node])
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
        for node in range(n):
            if disc[node] == -1:
                self.dfs(node, disc, low, parent,bridges, graph)
        return bridges
