import random

bank_dict = {}
bank_name = "中国工商银行北京市昌平区支行"


def welcome():
    print("***************************************************")
    print("**            中国工商银行账户管理系统v1.0           **")
    print("***************************************************")
    print("*【1】开户                                          *")
    print("*【2】存钱                                          *")
    print("*【3】取钱                                          *")
    print("*【4】转账                                          *")
    print("*【5】查询                                          *")
    print("*【6】退出系统                                       *")
    print("****************************************************")

#开户方法
def bank_adduser(number, username, passwork,contry, city, street, money,door):
    if len(bank_dict) >= 100:
        return 3
    if number in bank_dict:
        return 2

    bank_dict[number] = {
        "username": username,
        "passwork": passwork,
        "contry": contry,
        "city": city,
        "street": street,
        "money": money,
        "door":door
    }

    return 1
#开户
def adduser():
    number = random.randint(10000000, 99999999)
    username = input("请输入您的姓名:")
    passwork = int(input("请输入密码:"))
    print("请输入您的居住地址：")
    contry = input("\t\t国家：")
    city = input("\t\t省份：")
    street = input("\t\t街道：")
    door=input("请输入门牌号：")
    money = 0

    i = bank_adduser(number, username, passwork, contry, city, street, money,door)
    if i == 2:
        print("该账号已存在！请再试一次吧！")
    elif i == 3:
        print("该银行账号已满！请到其他支行吧！给您带来不便，非常抱歉！")
    elif i == 1:
        print("恭喜您！开通银行账户成功！")
        piao='''
                ______________用户信息记录______________
                账号：%s
                姓名：%s
                密码：**********
                国家：%s
                省份：%s
                街道：%s
                门牌号：%s
                余额：%s
                开户行：%s
                --------------------------------------
             '''

        print(piao%(number,username,contry,city,street,door,bank_dict[number]["money"],bank_name))
#存钱方法
def savemoney(number,passwork,money):
    if number in bank_dict:
        print("账号输入正确！")
        if passwork == bank_dict[number]["passwork"]:
            print("密码输入正确！")
            return True
        else:
            return False

    else:
        return False
#存钱
def cunqian():

    number = int(input("请输入您的账号："))
    passwork= int(input("请输入您的密码"))
    momey = int(input("请输入您要存的金额（整数）："))
    i=savemoney(number,passwork,momey)
    if i==True:
        bank_dict[number]["money"]=bank_dict[number]["money"]+momey
        print("存入了%d"%momey,"该账户余额为%d"%bank_dict[number]["money"])
    else:
        print("存款失败！可能是账号或密码错误")
#取钱方法
def qu_money(number, passwork, money):
    # 先根据账号信息来查询该用户是否存在，若不存在，则返回代号1，
    if number not in bank_dict:
        return 1
    # 若存在，则继续判断密码是否正确，若不正确，则返回代号2。
    if passwork !=bank_dict[number]["passwork"]:
        return 2
    # 若账号密码都正确，则继续判断当前用户的金额是否满足要取出的钱，若不满足，则返回代号3，
    if bank_dict[number]["money"]<money:
        return 3
    # 若满足，则将该用户的金额减去。
    bank_dict[number]["money"]=bank_dict[number]["money"]-money
    return 0
#取钱
def quqian():

    # 取钱（传入值：用户的账号，用户密码，取钱金额。
    # 返回值：整型值（0：正常，1：账号不存在，2：密码不对，3：钱不够））
    number = int(input("请输入您的账号："))
    passwork = int(input("请输入您的密码"))
    money = int(input("请输入您要取的金额（整数）："))
    i = qu_money(number, passwork, money)
    if i==1:
        print("账号不存在")

    elif i==2:
        print("密码不对")

    elif i==3:
        print("钱不够")

    elif i==0:
        print("该用户的金额减少了%d元"%money,"还剩%d"%bank_dict[number]["money"])
#转账方法
def zhuan_money(chu_number,chu_passwork,ru_number,chu_money):
    # 先查询用户库是否存在转出和转入的账号，若不存在则返回代号, 1，
    if chu_number not in bank_dict and ru_number not in bank_dict:
        return 1

    # 若账号都存在则继续判断转出账号的密码是否正确，若不正确，则返回2，
    if chu_passwork !=bank_dict[chu_number]["passwork"]:
        return 2
    # 若正确则继续判断要转出的金额是否足够，若不够则返回3，
    if chu_money > bank_dict[chu_number]["money"]:
        return 3
    # 否则正常转出，转出的账号用户金额要相对应的减少，转入的金额相对应的增加。
    bank_dict[chu_number]["money"]=bank_dict[chu_number]["money"]-chu_money
    bank_dict[ru_number]["money"]=bank_dict[ru_number]["money"]+chu_money
    print("转出账户金额少了%d"%chu_money,"还剩%d"%bank_dict[chu_number]["money"])
    print("转入账户金额多了%d" %chu_money,"还剩%d"%bank_dict[ru_number]["money"])

    return 0
#转账
def zhuanzhang():
    chu_number=int(input("请输入您要转出的账户号码："))
    chu_passwork=int(input("请输入您要转出的账户的密码："))
    ru_number = int(input("请输入您要转入的账户号码："))
    chu_money=int(input("请输入您要转出的金额："))
    i=zhuan_money(chu_number,chu_passwork,ru_number,chu_money)
    if i==1:
        print("账号不对")

    elif i==2:
        print("密码不对")

    elif i==3:
        print("钱不够")
    elif i==0:
        print("正常")
#查询方法
def inquire(number,passwork):
    # 先根据账号判断用户库是否存在该用户，若不存在则打印提示信息：该用户不存在。
    if number not in bank_dict:
        print("该用户不存在")
    # 否则继续判断密码是否正确。若不正确则打印相对应的错误信息。
    if passwork!= bank_dict[number]["passwork"]:
        print("密码输入错误")
    # 若账号和密码都正确，则将该用户的信息都打印出来，比如：当前账号：xxxx,密码:xxxxxx,余额：xxxx元，用户居住地址：xxxxxxxxxxxxx，当前账户的开户行：xxxxxxxxxx.
    print("查询成功一下是查询结果")
    info='''
            __________________用户信息__________________
            账号：%s                                   
            密码：%s                                   
            姓名：%s                                                                   
            国家：%s 
            省份：%s 
            街道：%s 
            门牌号：%s
            余额：%s 
            开户行：%s 
            -------------------------------------------
         '''
    print(info%(number,passwork,bank_dict[number]["username"],
                bank_dict[number]["contry"],bank_dict[number]["city"],
                bank_dict[number]["street"],bank_dict[number]["door"],bank_dict[number]["money"],bank_name))
# 查询
def chaxun():
    number=int(input("请输入账号："))
    passwork=int(input("请输入密码"))
    i= inquire(number,passwork)



while True:
    welcome()
    i = input("请输入您想操作的序号：")
    if i == "1":
        adduser()
    elif i == "2":
        cunqian()
    elif i == "3":
        quqian()
    elif i == "4":
        zhuanzhang()
    elif i == "5":
        chaxun()
    elif i == "6":
        print("欢迎再次使用中国工商银行账户管理系统！")
        break
    else:
        print("输入错误！请重新看看再输入要操作的序号！")
