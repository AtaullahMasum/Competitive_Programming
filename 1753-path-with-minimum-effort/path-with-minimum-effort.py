import heapq
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        heap = []
        rows, cols = len(heights), len(heights[0])
        dist = [[float('inf')]*cols for _ in range(rows)]
        direction= [(1,0),(-1,0),(0,1),(0,-1)]
        dist[0][0] = 0
        heapq.heappush(heap,(0,0,0))
        while heap :
            diff , u, v = heapq.heappop(heap)
            if u == rows -1 and v == cols -1:
                return diff
            for dr, dc in direction:
                nr, nc = dr+u, dc+v
                if  0<=nr<rows and 0<=nc<cols:
                    newEffort = max(abs(heights[u][v] - heights[nr][nc]), diff)
                    if newEffort < dist[nr][nc]:
                        dist[nr][nc] = newEffort
                        heapq.heappush(heap, (newEffort, nr, nc))
        