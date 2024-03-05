import heapq
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] != 0:
            return -1
        rows, cols = len(grid), len(grid[0])
        dist = [[float('inf')]*cols for _ in range(rows)]
        direction = [(1,0),(1,-1),(1,1),(-1,0),(-1,1),(-1,-1),(0,-1),(0,1)]
        dist[0][0] = 1
        queue = [(1,0,0)]
       
        while queue:
            cost , u, v = queue.pop(0)
            if u == rows-1 and v == cols-1:
                return dist[u][v]
            for nr, nc in direction:
                dr, dc = nr+u, nc + v
                if 0<=dr < rows and 0<=dc<cols and grid[dr][dc]==0 and dist[dr][dc]>1+dist[u][v]:
                    dist[dr][dc] = 1 + dist[u][v]
                    queue.append((dist[dr][dc],dr,dc))
        return -1
        if grid[0][0] != 0:
            return -1
        rows, cols = len(grid), len(grid[0])
        dist = [[float('inf')]*cols for _ in range(rows)]
        direction = [(1,0),(1,-1),(1,1),(-1,0),(-1,1),(-1,-1),(0,-1),(0,1)]
        dist[0][0] = 1
        heap = []
        heapq.heappush(heap,(1,0,0))
        while heap:
            cost , u, v = heapq.heappop(heap)
            if u == rows-1 and v == cols-1:
                return dist[u][v]
            for nr, nc in direction:
                dr, dc = nr+u, nc + v
                if 0<=dr < rows and 0<=dc<cols and grid[dr][dc]==0 and dist[dr][dc]>1+dist[u][v]:
                    dist[dr][dc] = 1 + dist[u][v]
                    heapq.heappush(heap,(dist[dr][dc],dr,dc))
        return -1
