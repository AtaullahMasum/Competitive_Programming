class DisjointSet:
    def __init__(self, V):
        self.parent = [i for i in range(V)]
        self.size = [1] * V

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
            self.parent[ult_pa_v] = ult_pa_u
            self.size[ult_pa_u] += self.size[ult_pa_v]

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        ds = DisjointSet(n * n)
        direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        # Step 1: applying disjoint set
        for row in range(n):
            for col in range(n):
                if grid[row][col] == 0:
                    continue
                for dr, dc in direction:
                    nr, nc = row + dr, col + dc
                    if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 1:
                        nodeno = row * n + col
                        adjacentnode = nr * n + nc
                        ds.unionBySize(nodeno, adjacentnode)
        
        # Step 2: calculate component sizes
        maximum_size = 0
        for row in range(n):
            for col in range(n):
                if grid[row][col] == 1:
                    continue
                components = set()
                for dr, dc in direction:
                    nr, nc = row + dr, col + dc
                    if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 1:
                        adjacentnode = nr * n + nc
                        components.add(ds.findUPa(adjacentnode))
                sizeTotal = sum(ds.size[node] for node in components) + 1
                maximum_size = max(maximum_size, sizeTotal)
        
        # Step 3: check individual cells
        for cellNo in range(n * n):
            maximum_size = max(maximum_size, ds.size[ds.findUPa(cellNo)])
        
        return maximum_size
