A = []
B = []
n,m = map(int, input().split())
for i in range(n):
    A.append(list(map(int,input().split())))

for i in range(n):
    B.append(list(map(int,input().split())))

def sumMatrix(A,B):
    answer = []
 
    for i in range(len(A)):
        tmp=[]
        for j in range(len(A[i])):
            tmp.append(A[i][j]+B[i][j])
        
        answer.append(tmp)
     
    return answer
for ans in sumMatrix(A,B):
    for i in ans:
        print(i, end=' ')
    print()