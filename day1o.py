class Car:
    num = 0
    color = ""
    brand = ""

    def run(self):
        print(self.brand,"=品牌的车在马路上跑")

car = Car()
car.num = 4
car.color = "绿色"
car.brand = "BWM"

car.run()


#题目二,学生类
class Person:
    __username = ""
    __age = 0

    def setAge(self,age):
        if age < 0 or age > 100:
            print("输入错误！")
        else:
            self.__age = age

    def getAge(self):
        return self.__age

    def setUsername(self,username):
        if username != "":
            self.__username = username
        else:
            print("用户名不能为空！")

    def getUsername(self):
        return self.__username


    def eat(self,eatName):
        print(self.__username,"正在吃",eatName)
    def sleep(self,hour):
        print(self.__username,"已经睡了",hour,"小时")
    def playGame(self,game):
        print(self.__username,"在玩游戏，玩的",game)
    def study(self,hour):
        print(self.__username,"正在学习，已经学了",hour,"小时")

p = Person()
p.setUsername("旺财")
p.setAge(56)


p.eat("四川小火锅")
p.sleep(6)
p.study(6)
p.playGame("绝地求生")

print(p.getAge())

#题目一，空调类
class conditioner:
    __brand = ""
    __price = 0

    def setBrand(self,brand):
        self.__brand = brand

    def getBrand(self,brand):
        return self.__brand

    def setPrice(self,price):
        if price < 0:
            print("输入非法！")
        else:
            self.__price = price

    def getPrice(self,price):
        return self.__price


    def open(self):
        print("空调开机了...")
    def close(self, hour):
        print("空调将在", hour, "分钟后自动关闭")

c = conditioner()
c.setBrand("格力")
c.setPrice(10000)

c.open()
c.close(5)

#题目三，猴子类
class monkey:
    category = ""
    sex = ""
    color = ""
    weight = ""

    def setCategory(self,category):
        if category != "金丝猴" or category != "叶猴":
            print("猴子不存在！")
        else:
            self.category = category

    def getCategory(self,category):
        return self.category

    def setSex(self,sex):
        if sex != "公" or sex != "母":
            print("猴子有毒！")
        else:
            self.sex = sex

    def getSex(self,sex):
        return self.sex

    def setColor(self,color):
        self.color = color

    def getColor(self,color):
        return self.color

    def setWeight(self,weight):
        self.weight = weight

    def getWeight(self,weight):
        return self.weight

    def action(self,material):
        print("这只猴子在用",material,"搞火！")

    def learn(self,things):
        print("这只猴子在学",things)


m = monkey()
m.setCategory("金丝猴")
m.setSex("公")
m.setColor("灰色")
m.setWeight("100斤")

m.action("木棍")
m.learn("摘果子")
























