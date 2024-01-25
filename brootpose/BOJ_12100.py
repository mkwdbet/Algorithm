import numpy as np 
N = int(input())
class Board():
    def __init__(self,N):
        self.board = np.zeros((N,N))
        print(self.board)

    def setPoint(self,point,value):
        self.board[point[0],point[1]] = value

    def keyLeft(self):
        for i in range(N):
            prevValue = 0
            prevPoint = []
            for j in range(N):
                if prevValue == self.board[i,j]:
                    self.setPoint(prevPoint, prevValue *2)
                    self.setPoint([i,j],0)
                    cnt += 1
                    continue
                if cnt > 0:
                    self.setPoint([i,j-cnt],self.board[i,j])
                    self.setPoint([i,j],0) 
                cnt +=1
                prevValue = self.board[i,j]
                prevPoint = [i,j]
                        
a = Board(N)