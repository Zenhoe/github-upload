import random
i = [1,2,3]
x = 1,2,3,4
ranNum = str(input())
Fuckoff = int(input("How many numbers do you want: "))
list_num = ranNum
for i in range(Fuckoff):
    random.shuffle(list_num)
    print(list_num[1])


