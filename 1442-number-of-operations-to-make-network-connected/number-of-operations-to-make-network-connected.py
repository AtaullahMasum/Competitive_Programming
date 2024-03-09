class DisjointSet:
  def __init__(self, V):
    self.parent = [i for i in range(V+1)]
    self.rank = [0]*(V+1)
  def findUPa(self, node):
    if node == self.parent[node]:
      return node
    self.parent[node] = self.findUPa(self.parent[node])
    return self.parent[node]
  def unionByRank(self, u, v):
    ult_pa_u = self.findUPa(u) # ultimate parent of u
    ult_pa_v = self.findUPa(v) # ultimate parent of v
    if ult_pa_u == ult_pa_v:
      return
    if self.rank[ult_pa_u] < self.rank[ult_pa_v]:
      self.parent[ult_pa_u] = ult_pa_v
    elif self.rank[ult_pa_v] < self.rank[ult_pa_u]:
      self.parent[ult_pa_v] = ult_pa_u
    else:
      self.parent[ult_pa_v] =  ult_pa_u
      self.rank[ult_pa_u] += 1
class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n-1:
            return -1
        graph = [[] for _ in range(n)]
        for u,v in connections:
            graph[u].append(v)
            graph[v].append(u)
        visited = [0]*n
        def dfs(node):
            visited[node] = 1
            for adjacent in graph[node]:
                if not visited[adjacent]:
                    dfs(adjacent)
        count = 0
        for i in range(n):
            if not visited[i]:
                dfs(i)
                count += 1
        return count-1
        #using DisjointSet
        ds = DisjointSet(n)
        extraedges = 0
        for u, v in connections:
            if ds.findUPa(u)==ds.findUPa(v):
                extraedges += 1
            else:
                ds.unionByRank(u,v)
        numberofcomponent = 0
        for i in range(n):
            if ds.findUPa(i) == i:
                numberofcomponent += 1
        ans = numberofcomponent - 1
        if extraedges >= ans:
            return ans
        return -1

        