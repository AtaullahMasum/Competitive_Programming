class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = [[] for _ in range(n)]
        for u,v,price in flights:
            graph[u].append((v,price))
        dist = [float('inf')] *n
        dist[src] = 0
        queue = [(0,src,0)]
        while queue:
            stops, node, cost = queue.pop(0)
            if stops > k:
                continue
            for adjacent, weight in graph[node]:
                if weight + cost < dist[adjacent] and stops <= k:
                    dist[adjacent] = weight + cost
                    queue.append((stops+1, adjacent, dist[adjacent]))
        if dist[dst] == float('inf'):
            return -1
        return dist[dst]



