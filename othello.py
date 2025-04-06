import sys;sys.stdin=open('othello.txt')
T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    matrix = [[0] * N for _ in range(N)]

    mid = N//2

    for z in range(2):
        matrix[mid+z-1][mid-z] = 1
        matrix[mid+z-1][mid+z-1] = 2

    dx,dy = [0,1,1,1,0,-1,-1,-1],[1,1,0,-1,-1,-1,0,1]
    for _ in range(M):
        x, y, player = map(int,input().split())
        x,y = x-1,y-1

        if player == 1:
            matrix[x][y] = 1
            for i in range(8):
                temp = []
                for j in range(1,N):
                    nx = x + dx[i]*j
                    ny = y + dy[i]*j
                    if 0 <= nx < N and 0 <= ny < N:
                        if matrix[nx][ny] == 2:
                            temp.append((nx,ny))
                        elif matrix[nx][ny] == 1:
                            for a,b in temp:
                                matrix[a][b] = 1
                            break
                        else:
                            break
                    else:
                        break
        else:
            matrix[x][y] = 2
            for i in range(8):
                temp = []
                for j in range(1,N):
                    nx = x + dx[i]*j
                    ny = y + dy[i]*j
                    if 0 <= nx < N and 0 <= ny < N:
                        if matrix[nx][ny] == 1:
                            temp.append((nx,ny))
                        elif matrix[nx][ny] == 2:
                            for a,b in temp:
                                matrix[a][b] = 2
                            break
                        else:
                            break
                    else:
                        break


    black_cnt = 0
    white_cnt = 0
    for r in range(N):
        for c in range(N):
            if matrix[r][c] == 1:
                black_cnt += 1
            elif matrix[r][c] == 2:
                white_cnt += 1

    print(f'#{tc} {black_cnt} {white_cnt}')

