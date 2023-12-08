import pyinputplus as pyip
import random

min = 1
max = 100
count = 0

random_number =random.randint(min,max)
print(random_number)
print("==========猜數字遊戲==============")

while(True):

    keyin = pyip.inputInt(f"請輸入數字{min}~{max}")
    count += 1
    print(keyin)

    if keyin == random_number:
        print(f"恭喜猜對了,答案是{random_number}")
        break
    elif keyin > random_number:
        print("再小一點")
        max = keyin - 1
    elif keyin < random_number:
        print("再大一點")
        min = keyin + 1
    print(f"你已經猜了{count}次")
    print("=========================================")

print("程式結束")