import heapq
class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        # Build graph
        graph = [[] for _ in range(n)]
        for u, v, weight in roads:
            graph[u].append((v, weight))
            graph[v].append((u, weight))
        
        # Initialize distance and ways arrays
        dist = [float('inf')] * n
        ways = [0] * n
        ways[0] = 1
        dist[0] = 0
        
        # Initialize heap with source node
        heap = [(0, 0)]  # (distance, node)
        
        # Dijkstra's algorithm
        while heap:
            cost, node = heapq.heappop(heap)
            if cost > dist[node]:
                continue
            for adjacent, weight in graph[node]:
                if dist[adjacent] > weight + dist[node]:
                    dist[adjacent] = weight + dist[node]
                    heapq.heappush(heap, (dist[adjacent], adjacent))
                    ways[adjacent] = ways[node]  # Update ways array with the number of ways from the current node
                elif dist[adjacent] == weight + dist[node]:
                    ways[adjacent] = (ways[adjacent] + ways[node]) % (10 ** 9 + 7)  # Accumulate ways from all possible paths
        
        return ways[n - 1] %(10 ** 9 + 7) 
        graph = [[] for _ in range(n)]
        for u, v, weight in roads:
            graph[u].append((v, weight))
            graph[v].append((u, weight))
        ways = [0]*n
        dist = [float('inf')]*n
        ways[0] = 1
        dist[0] = 0
        heap = []
        heapq.heappush(heap,(0, 0)) #distance, src
        while heap:
            cost, node = heapq.heappop(heap)
            for adjacent, weight in graph[node]:
                if dist[adjacent] > weight + dist[node]:
                    dist[adjacent] = weight + cost
                    heapq.heappush(heap,(weight + cost, adjacent))
                    ways[adjacent] = ways[node]
                elif dist[adjacent] == weight + dist[node]:
                    ways[adjacent] = (ways[adjacent]+ways[node])%(10**9+7)
        return ways[n-1]%(10**9+7)


        