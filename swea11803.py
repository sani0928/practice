import sys;sys.stdin=open('swea11803.txt')

def move(idx, depth, total):
    global min_val

    if total > min_val:
        return

    if depth == N:
        min_val = min(min_val, total + matrix[idx][0])
        return

    for i in range(1,N):
        if not visited[i]:
            visited[i] = True
            move(i, depth + 1, total + matrix[idx][i])
            visited[i] = False

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    min_val = float('inf')

    visited = [False] * N
    visited[0] = True
    move(0, 1, 0)

    print(f'#{tc} {min_val}')