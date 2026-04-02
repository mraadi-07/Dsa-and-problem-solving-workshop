num = 12345
a = num % 10# 5
num = num // 10 # 1234
b = num % 10# 4
num = num // 10 # 123
c = num % 10# 3
num = num // 10 # 12
d = num % 10# 2
num = num // 10 # 1
e = num# 1
rev = a*10000 + b*1000 + c*100 + d*10 + e
print(rev)