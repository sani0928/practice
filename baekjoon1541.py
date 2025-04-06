import sys;sys.stdin=open('baekjoon1541.txt')

sik = list(map(str,input()))
print(len(sik))
i = 0
while i < len(sik):

    if sik[i] == '-':
        sik.insert(i,'(')
        for j in range(i+2,len(sik)):
            if sik[j] == '-':
                sik.insert(j, ')')
                i = j
                break

    i += 1

print(sik)

