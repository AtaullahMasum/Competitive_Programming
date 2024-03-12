import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = [[] for _ in range(n+1)]
        for  u, v, weight in times:
            graph[u].append((v, weight))
        dist = [float('inf')]*(n+1)
        dist[k] = 0
        heap = []
        heapq.heappush(heap,(0, k))
        while heap:
            cost , node = heapq.heappop(heap)
            for adjacent_node, weight in graph[node]:
                if dist[adjacent_node] > dist[node] + weight:
                    dist[adjacent_node] = dist[node] + weight
                    heapq.heappush(heap, (dist[adjacent_node], adjacent_node))
        time = 0
        for i in range(1,n+1):
            if dist[i]== float('inf'):
                return -1
            time = max(time, dist[i])
        return time


        