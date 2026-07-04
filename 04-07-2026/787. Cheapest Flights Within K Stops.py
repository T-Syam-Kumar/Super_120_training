def findcheapest(n,flight,src,dst,k):
    distance = [float('inf')]*n
    distance[src] = 0
    for i in range(k+1):
        temp = distance.copy()
        for u,v,w in flight:
            if distance[u] == float('inf'):
                continue
            if distance[u]+w < temp[v]:
                temp[v] = distance[u]+w
        distance = temp.copy()
    return distance[dst] if distance[dst] != float('inf') else -1