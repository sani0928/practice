import sys;sys.stdin=open('baekjoon1238.txt')
import heapq

def dijkstra(s):
    heap = [(0,s)]
    dists = [INF] * (N+1)
    dists[s] = 0

    while heap:

        dist, node = heapq.heappop(heap)

        if dists[node] < dist:
            continue

        for next in graph[node]:
            next_dist = next[0] # w
            next_node = next[1] # e

            new_dist = dist + next_dist

            if dists[next_node] <= new_dist:
                continue

            dists[next_node] = new_dist
            heapq.heappush(heap, (new_dist, next_node))


    return dists

N,M,X = map(int,input().split())
graph = [[] for _ in range(N+1)]
INF = float('inf')
for _ in range(M):
    s, e, w = map(int,input().split())
    graph[s].append((w,e))

dist_to_X = [0] + [dijkstra(i)[X] for i in range(1,N+1)]

dist_from_X = dijkstra(X)

max_result = 0
for i in range(1,N+1):
    max_result = max(max_result, (dist_to_X[i] + dist_from_X[i]))

print(max_result)