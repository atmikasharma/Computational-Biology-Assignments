n=94
m=17

rab_num = [0]*m
offspring = 0
summ = 0
value = 0
rab_num[0] = 1
for i in range(0, n-1):
    offspring = sum(rab_num[1:m])
    rab_num = [offspring] + rab_num[0:m-1]
print(sum(rab_num))