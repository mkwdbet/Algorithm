def isHanNum(N):
    cnt = 0
    for i in range(1,N+1):
        if i < 100:
            cnt +=1
            continue
        str_i = str(i)
        if (int(str_i[0]) + int(str_i[2])) / 2 == int(str_i[1]):
            cnt += 1
    return cnt
N = int(input())
print(isHanNum(N))



        