import sys;sys.stdin=open('baekjoon13418.txt')
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a,b):

    root_a = find(a)
    root_b = find(b)

    if root_a != root_b:
        parent[root_b] = root_a

N,M = map(int,input().split())
edges = []


s, e, w = map(int,input().split())
edges.append((w,s,e))

for _ in range(M):
    a, b, c = map(int,input().split())
    edges.append((c,a,b))

edges_max = sorted(edges, key = lambda x : x[0])
edges_min = sorted(edges, reverse=True, key = lambda x : x[0],)

cnt_max = 0
cnt_min = 0

parent = [i for i in range(N+1)]
for w,s,e in edges_max:
    if find(s) != find(e):
        union(s, e)
        if w == 0:
            cnt_max += 1

parent = [i for i in range(N+1)]
for w,s,e in edges_min :
    if find(s) != find(e):
        union(s, e)
        if w == 0:
            cnt_min += 1

result = (cnt_max**2) - (cnt_min**2)

print(result)

