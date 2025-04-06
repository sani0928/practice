import sys;sys.stdin=open('baekjoon1647.txt')
import heapq
input = sys.stdin.readline

def dijkstra(start):

    pq = [(0,start)]
    dists = [INF] * (N+1)
    parent = [i for i in range(N+1)]
    dists[start] = 0

    while pq:

        cost, node = heapq.heappop(pq)

        if dists[node] < cost:
            continue

        for next in graph[node]:
            next_cost = next[0]
            next_node = next[1]

            new_cost = cost + next_cost

            if dists[next_node] <= new_cost:
                continue

            dists[next_node] = new_cost
            print(dists)
            parent[next_node] = node
            heapq.heappush(pq, (new_cost, next_node))

    return parent

N, M = map(int,input().split())
INF = float('inf')

graph = [[] for _ in range(N+1)]

for _ in range(M):
    u,v,w = map(int,input().split())
    graph[u].append((w,v))
    graph[v].append((w,u))
print(graph)
parent = dijkstra(1)

result = []
for i in range(2,N+1):
    result.append((parent[i],i))

print(len(result))
for a, b in result:
    print(a, b)