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
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        ds = DisjointSet(n)
        mapMailNode = {}
        for i in range(n):
            for j in range(1,len(accounts[i])):
                mail = accounts[i][j]
                if mail not in mapMailNode:
                    mapMailNode[mail] = i
                else:
                    ds.unionBySize(i, mapMailNode[mail])
        mergeMailNode = [[] for _ in range(n)]
        for mail, values in mapMailNode.items():
            node = ds.findUPa(values)
            mergeMailNode[node].append(mail)
        ans = []
        for i in range(n):
            if len(mergeMailNode[i]) == 0:
                continue
            mergeMailNode[i].sort()
            temp = [accounts[i][0]]  # Add the name to the temp list
            temp.extend(mergeMailNode[i])  # Extend the temp list with the merged mails
            ans.append(temp)
        return ans



        
        