class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        dist = [[float('inf')]*n for _ in range(n)]
        for u,v,weight in edges:
            dist[u][v] = weight
            dist[v][u] = weight
        for i in range(n):
            dist[i][i] = 0
        for k in range(n):
            for i in  range(n):
                for j in range(n):
                    if dist[i][k] == float('inf') or dist[k][j]==float('inf'):
                        continue
                    dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])
        countcity = n
        cityno = -1
        for city in range(n):
            count = 0
            for adjacent_city in range(n):
                if dist[city][adjacent_city] <=  distanceThreshold:
                    count += 1
            if countcity >= count:
                countcity = count
                cityno = city
        return cityno
