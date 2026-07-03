import collections
def findCheapestPrice(n, flights, src, dst: int, k: int) -> int:
        adj = collections.defaultdict(list)
        for u, v, w in flights:
            adj[u].append((v, w))
            
        min_cost = [float('inf')] * n
        min_cost[src] = 0
        
        queue = collections.deque([(0, src, 0)]) # (stops, node, cost)
        
        while queue:
            stops, u, cost = queue.popleft()
            if stops > k: continue
            
            for v, w in adj[u]:
                if cost + w < min_cost[v]:
                    min_cost[v] = cost + w
                    queue.append((stops + 1, v, min_cost[v]))
                    
        return min_cost[dst] if min_cost[dst] != float('inf') else -1