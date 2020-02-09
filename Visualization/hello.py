print("hello world")

names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)

height = 1.75
weight = 80.5
name = weight/height

if name <= 18.5:
    print("light")
elif name > 18.5 and name <= 25:
    print("little")
elif name > 25 and name <=28:
    print("big")
elif name > 28 and name <=32:
    print("Bbig")
else:
    print("BBbig")

sum = 0
for i in range(10001):
    sum = sum + i
print(sum)

a = abs(-100)
print(a)

def my_abs(x):
    if x > 0:
        return x
    else:
        return -x

print(my_abs(-199))

def my_hanshu(x):
    pass

def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)

print(fact(100))

print("千寻你好，人们叫我'无脸男' \n这个世界的人都选择无视我\n只有你看到了我并和我打招呼\n我感到很孤单，很孤单\n你愿意和我成为朋友吗？")