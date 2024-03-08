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
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        #Solution 1
        rows = len(isConnected)
        cols = len(isConnected[0])
        adjList = [[] for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if isConnected[i][j] == 1 and i != j:
                    adjList[i].append(j)
                    adjList[j].append(i)
        count = 0
        visited = [0]*rows
        def dfs(node):
            visited[node] = 1
            for i in adjList[node]:
                if not visited[i]:
                    dfs(i)
        for i in range(rows):
            if not visited[i]:
                count +=1
                dfs(i)
        return count
        #Solution 2
        V = len(isConnected)
        ds = DisjointSet(V)
        for i in range(V):
            for j in range(V):
                if isConnected[i][j] == 1:
                    ds.unionByRank(i,j)
        count = 0
        for i in range(V):
            if ds.findUPa(i) == i:
                count += 1
        return count


        