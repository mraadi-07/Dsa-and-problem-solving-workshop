# logic : iterate through the dictionary and keep track of the key with the minimun value 
# input : {"X":20, "Y":10, "Z":30}
# # output : "Y"
# ip = {"x":20,"y":10,"z":30 }
# op = min(ip, key=ip.get)
# print(op)

# mydict = {101:"Aditya",
#           "profession":"developer",
#           "empid":12345,}
# mydict.pop(101)
# print(mydict)

# n = int(input("enter the number of rows: "))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j, end=" ")
#     print()

# n = int(input("enter the number of rows: "))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(chr(64+i), end=" ")
#     print()

# n = int(input("enter the number of rows: "))
# for i in range(1,n+1):     
#     for j in range(1,n+2-i):     
#         print(chr(64+j), end=" ")
#     print()

# import time
# n=int(input("enter the number of rows:"))
# for i in range(1,n+1):
#     for j in range(1,n+1-i):
#         time.sleep(1)
#         print(n+1-i,end= " ")
#     print()

# import time
# n = int(input("enter the number of rows: "))
# for i in range(1,n+1): 
#     print(" "*(n-i),end=" ")          #n+1=6 
#     for j in range(1,i+1):
#         time.sleep(1)
#         print("*", end=" ")     
#     print()

# def msg():
#     print("Hello world")
# msg()
# msg()

# def arithmetic():
#     a = int(input("Enter the value of A :"))
#     b = int(input("Enter the value of B :"))
#     add = a+b
#     sub = a-b
#     mul = a*b
#     div = a/b
#     return add,sub,mul,div
# # print(arithmetic())
# result = arithmetic()
# print("Arithmetic =",result)

# how many type of argument we can pass in fnction
# 1. positional argument
# 2. keyword argument
# 3. default argument
# 4. varable number of argument/ variable length argument

# # positional argument
# def login(username, password):
#     if username == password:
#         print("Login successfully")
#     else:
#         print("Invalid creditial")
# username = input("Enter Username : ")
# password = input("Enter password : ")
# login(username,password)

# keyword argument
# def login(username, password):
#     if username == password:
#         print("Login successfull")
#     else:
#         print("Invalid ")
# login(username="admin", password="admin")

# default argument
# def cityname(city = "goa"):
#     print(city)
# cityname("Delhi")
# cityname("Kolhapur")
# cityname()

# variable length argument/ varibale number ..
# def nameofcitys(*city):
#     print("city name =", city)
# nameofcitys("goa","Nagpur","Mumbai","Pune","Nashik")

#wap for menu driven code
import sys
def add():
    v1=int(input("enter value for v1:"))
    v2=int(input("enter value for v2:"))
    print("Add:",v1+v2)

def sub():
    v1=int(input("enter value for v1:"))
    v2=int(input("enter value for v2:"))
    print("Sub:",v1-v2)

def mul():
    v1=int(input("enter value for v1:"))
    v2=int(input("enter value for v2:"))
    print("Mul:",v1*v2)

def div():
    v1=int(input("enter value for v1:"))
    v2=int(input("enter value for v2:"))
    print("Div:",v1/v2)

while True:
    print("1.Addition")
    print("2.Substraction")
    print("3.Multiplication")
    print("4.Divison")
    print("5.Exit")

    choice = int(input("Enter your choice:"))

    if choice == 1:
        add()
    elif choice == 2:
        sub()
    elif choice == 3:
        mul()
    elif choice == 4:
        div()
    elif choice == 5:
        sys.exit()