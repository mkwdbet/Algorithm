import numpy as np 

array = []
for i in range(9):
    array.append(list(map(int,input().split())))
board = np.array(array)
max =board.max()
idx = np.where(board == max)
print(max)
print(int(idx[0]))