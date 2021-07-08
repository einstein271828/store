

def add(a,b):
    c=a+b
    return c
a=6
b=5
c=add(a,b)

print(c)
##



for i in range(1,10):
    for j in range(1,i+1):
       print(j,"X",i,"=",(j*i),"\t",end="")
    print()



def printNxN(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,"x",i,"=",(j*i),"\t",end="")
        print()
n = input("请输入您要的乘法表层数：")
printNxN(int(n))

























