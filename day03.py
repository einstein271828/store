import random

data=random.randint(0,100)
coin=5000
i=0
while i<=10:
    num=input("请输入要猜的数字：")
    num=int(num)
    if num>data:
        print("大了")
        coin=coin-500
        print("当前硬币数为：",coin)
    elif num<data:
        print("小了")
        coin=coin-500
        print("当前硬币数为：",coin)
    else:
        print("恭喜您，猜中数字，本次幸运数字为：",num,"您猜了多少次：",i)
        coin=coin+2000
        print("您所拥有的硬币为：",coin)
        break
    i=i+1
