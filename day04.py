import random
shop=[
    ["机械革命",15000],
    ["HUAWEI watch",1200],
    ["MAC PC",13000],
    ["水杯",30],
    ["橙汁",5],
    ["可口可乐",3]
]
xiaopiao=[
         ['机械革命',0.9],
         ["HUAWEI watch",0.9],
         ["MAC PC",0.9],
         ["水杯",0.5],
         ["橙汁",0.5],
         ["可口可乐",0.5]
]
print("欢迎来到昌平商城")
money=input("请输入您的现金余额：")
money=int(money)
piao=random.randint(0,len(xiaopiao)-1)
print("您获得本商城的折扣序号为：",xiaopiao[piao])
zheko=xiaopiao[piao][1]
print("您享受的是%.2f"%zheko,"优惠")
mycart = []

while True:
    for index,value in enumerate(shop):
        print(index,"   ",value)

    chose = input("请输入您要的商品：")

    if chose.isdigit():
        chose=int(chose)
        if chose > len(shop)-1 or chose<0:
            print("您要的商品不存在！")
        else:
            if money < shop[chose][1]:
                print("对不起，余额不足！")
            else:
                if chose==piao:
                    mycart.append(shop[chose])
                    jiaoge=shop[chose][1]*zheko
                    money = money-jiaoge
                    print("你还剩，￥",money)
                else:
                    mycart.append(shop[chose])
                    money = money-shop[chose][1]
                    print("您还剩,￥",money)

    elif chose == 'q' or chose =='Q':
        print("欢迎下次光临！")
        break
    else:
        print("对不起，您输入的商品不存在！")




print("请拿好你的小票！")
for index,value in enumerate(mycart):
         print(index,"   ",value)
         print("您的钱包还剩：￥",money)



