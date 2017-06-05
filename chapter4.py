a=str(123)
for b in a:
    print("char in a",b)

#字符串作为一个字符的数组集合,集合的下标是重0开始的
for i in range(0,len(a)):
    print(a[i])
#字符的切分:类似java中的子字符串
print(a[1:3])
print(a[0:4])
#python中相对于java中特有的负数的索引，意指倒数第几个字符
print(a[0:-2])
#扩展分片
#复制字符串
b=a[:]
print(b)

# ord（） ：显示单个字符对应的ASCII码
# chr():显示对应数字的字符



print(chr(97))