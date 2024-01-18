len_list ,stopNum  = map(int, input().split())
num_list = list(map(int, input().split()))
num_list.sort(reverse=True) #내림차순 정렬

def draw_bestnum(len_list, stopNum, num_list):
    for i in range(len_list):
        sum = num_list[i]
        cnt = 1 
        for j in range(i+1,len_list):
            if sum + num_list[j] <= stopNum and cnt < 3:
                sum += num_list[j]
                cnt += 1
            if cnt == 3:
                return sum
print(draw_bestnum(len_list, stopNum, num_list))

                