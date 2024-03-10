class DisjointSet:
    def __init__(self, V):
      self.parent = [i for i in range(V+1)]
      self.size = [1]*(V+1)
    def findUPa(self, node):
      if self.parent[node] == node:
        return node
      self.parent[node] = self.findUPa(self.parent[node])
      return self.parent[node]

    def unionBySize(self, u, v):
      ult_pa_u = self.findUPa(u)
      ult_pa_v = self.findUPa(v)
      if ult_pa_u == ult_pa_v:
        return
      if self.size[ult_pa_u] < self.size[ult_pa_v]:
        self.parent[ult_pa_u] = ult_pa_v
        self.size[ult_pa_v] += self.size[ult_pa_u]
      else:
        self.parent[ult_pa_u] = ult_pa_v
        self.size[ult_pa_u] += self.size[ult_pa_v]
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        maxRows = 0
        maxCols = 0
        n = 0
        for row, col in stones:
            maxRows = max (maxRows, row)
            maxCols = max (maxCols, col)
            n += 1
        ds = DisjointSet(maxRows+maxCols+1)
        uniqueNodes = {}
        for row, col in stones:
            rowNode = row
            colNode = col + maxRows + 1
            ds.unionBySize(rowNode, colNode)
            uniqueNodes[rowNode] = 1
            uniqueNodes[colNode] = 1
        count = 0
        for node, values in uniqueNodes.items():
            if ds.findUPa(node) == node:
                count += 1
        return n - count

        