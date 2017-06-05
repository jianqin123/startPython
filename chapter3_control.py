a=range(1,10)
for b in a :
    print(b)

# must  be integers
for c in range(5,10,1):
    if(c<6):
        print("c",c)
    elif(c<8):
        print("c2",c)
    else:print(c)
a=10
while(a>0):
    print(a)
    a-=2


#多重复制
a,b,c=1,2,3
print(a,b,c)

#交换
a,b=1,2
a=b
b=a
print("第一次交换：",a,"->",b)

a,b=1,2
temp=a
a=b
b=temp
print("第二次交换：",a,"->",b)

for b in "sdfasd":
    print("char in string ",b)


