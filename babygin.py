import sys;sys.stdin=open('babygin.txt')

def babygin(player):

    # triplet
    for j in range(len(player) - 2):
        if player[j] == player[j + 1] == player[j + 2]:
            return True

    # run
    player = list(set(player))
    for j in range(len(player) - 2):
        if player[j] == player[j + 1] - 1 == player[j + 2] - 2:
            return True

    return False

T = int(input())
for tc in range(1,T+1):
    lst = list(map(int,input().split()))

    p1 = []
    p2 = []

    p1win = False
    p2win = False

    for i in range(len(lst)):

        if p1win or p2win:
            break

        if i % 2 == 0:
            p1.append(lst[i])
            p1.sort()
            i += 1
            if len(p1) >= 3:
                if babygin(p1):
                    p1win = True
                    break

        else:
            p2.append(lst[i])
            p2.sort()
            i += 1
            if len(p2) >= 3:
                if babygin(p2):
                    p2win = True
                    break

    if p1win:
        print(f'#{tc} {1}')
    elif p2win:
        print(f'#{tc} {2}')
    else:
        print(f'#{tc} {0}')
