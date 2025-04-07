import heapq

def dijkstra(dist,start_node,end_node):

    pq =[(dist,start_node)]
    dists = [INF] * (N + 1)
    dists[start_node] = 0

    while pq:
        dist, node = heapq.heappop(pq)

        if dists[node] < dist:
            continue

        for next in graph[node]:
            next_dist = next[0]
            next_node = next[1]

            new_dist = dist + next_dist

            if dists[next_node] > new_dist:
                dists[next_node] = new_dist
                heapq.heappush(pq, (new_dist,next_node))

    return dists[end_node]

N,M,X = map(int,input().split())
graph = [[] for _ in range(N+1)]
INF = float('inf')

for _ in range(M):
    u,v,w = map(int,input().split())
    graph[u].append((w,v))

max_result = 0

for i in range(1,N+1):
    temp1 = dijkstra(0,i,X)
    temp2 = dijkstra(0, X, i)
    max_result = max(max_result, temp1+temp2)


print(max_result)