class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        graph = defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))
        
        pq = [(0, src, 0)]  # (cost, node, stops)
        visited = [float('inf')] * n
        
        while pq:
            cost, node, stops = heapq.heappop(pq)
            if node == dst:
                return cost
            if stops > k or stops >=visited[node] :
                continue
            visited[node] = stops
            for neighbor, neighbor_cost in graph[node]:
                heapq.heappush(pq, (cost + neighbor_cost, neighbor, stops + 1))
        
        return -1
        INF = float('inf')
        dp = [[INF] * n for _ in range(k + 2)]  # K stops + 1 and destination
        dp[0][src] = 0

        for i in range(1, k + 2):
            dp[i][src] = 0  # Base case: no cost to reach source

        for i in range(1, k + 2):
            for u, v, w in flights:
                dp[i][v] = min(dp[i][v], dp[i - 1][u] + w)

        return dp[k + 1][dst] if dp[k + 1][dst] != INF else -1