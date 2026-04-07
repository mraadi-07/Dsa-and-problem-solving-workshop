# Logic : use loops to count concicutive characters and create the  compressed string
# input : "aaabbbccc"
# output : "3a3b3c"
# code :

# string = "aaabbbccc"
# newstring = ""
# count = 1
# for i in range(len(string)-1):
#     if string[i] == string[i+1]:
#         count = count + 1
#     else:
#         newstring = newstring + str(count) + string[i]
#         count = 1
# newstring = newstring + str(count) + string[len(string)-1]
# print(newstring)

# ----------------------------------------------------------------------------------

# logic : split the string into words, revers each word and join them back together
# input : "hello world"
# output : "olleh dlrow"
# Code : 

# string = "hello world"
# words = string.split(" ")
# newwords = []
# for i in words:
#     newwords.append(i[::-1])
# newstring = " ".join(newwords)
# print(newstring)

# ----------------------------------------------------------------------------------

# from abc import ABC, abstractmethod
# class help4code(ABC):
#     @abstractmethod #decorator
#     def training(self):
#         pass
#     @abstractmethod
#     def placement(self):
#         pass
# class Aditya(help4code):
#     def training(self):
#         print("c, c++, python")
#     def placement(self):
#         print("Python placement")
# class Ankit(help4code):
#     def training(self):
#         print("Python, java")
#     def placement(self):
#         print("Java placement")
# class Vishal(help4code):
#     def training(self):
#         print("practice learning")
#     def placement(self):
#         print("Data science placement")
# obj1 = Aditya()
# obj1.training()
# obj1.placement()
# obj2 = Ankit()
# obj2.training()
# obj2.placement()
# obj3 = Vishal()
# obj3.training()
# obj3.placement()

# ----------------------------------------------------------------------------------

# from abc import ABC,abstractmethod
# class Irctc(ABC):
#     @abstractmethod
#     def bookticket(self):
#         pass

# class Makemytrip(Irctc):
#     def bookticket(self):
#         print("=============================================")
#         print("welcom to makemytrip.com")
#         sorce = input("Enter a source station name:")
#         destination = input("Enter a destination station name:")
#         date = input("Enter date:")
#         print("=============================================")

# class Goibibo(Irctc):
#      def bookticket(self):
#         print("=============================================")
#         print("welcom to Goibibo.com")
#         sorce = input("Enter a source station name:")
#         destination = input("Enter a destination station name:")
#         date = input("Enter date:")
#         print("=============================================")

# class yatra(Irctc):
#      def bookticket(self):
#         print("=============================================")
#         print("welcom to yatra.com")
#         sorce = input("Enter a source station name:")
#         destination = input("Enter a destination station name:")
#         date = input("Enter date:")
#         print("=============================================")

# obj1 = Makemytrip()
# obj2 = Goibibo()
# obj3 = yatra()
# obj1.bookticket()
# obj2.bookticket()
# obj3.bookticket()

# --------------------------------------------------------------------------------

# class base:
#     def __init__(self):
#         print("Parent class constructor called")
#         self.a = "Aditya" # public data member
#         self.__c = "Vishal" # private data member
# # creating a derived class/ child class
# class Derived(base):
#     def __init__(self):
#         # calling constructor of base class
#         base.__init__(self)
#         # print("calling private member of base class:")
#         # print(self.a)
#         # print(self.__c)
# # obj1 = Derived()
# # print(obj1.a)
# # print(obj1.__c)
# obj2 = base()
# print(obj2.a) #accessable
# print(obj2.__c) # not accessable

# --------------------------------------------------------------------------------

# class Rbi:
#     #delcaring public method
#     def publicPolicy(self):
#         print("check public poliocy of Rbi")

#     #declaring private method
#     def __privatepolicy(self):
#         print("there is some private policy which is not accesible for public")

# class Sbi(Rbi):
#     def __init__(self): #first sbi class const called
#         Rbi.__init__(self) #second parent class constr called
    
#     def callingPublicMethod(self): #childclass public method
#         print("calling public method")
#         self.publicPolicy() #calling parentclass public method

#     def callingPrivateMethod(self): #childclass public method
#         self.privatePolicy() #calling parentclass private method

# # obj1 = Sbi()
# # obj1.callingPublicMethod()
# # obj1.callingPrivateMethod()
# # obj1.publicPolicy()
# # obj1.__privatepolicy()
# obj2 = Rbi()
# obj2.publicPolicy()
# obj2.__privatepolicy
# # obj2 = Rbi()
# # obj2.publicPolicy()
# # obj2._Rbi__privatepolicy()

# --------------------------------------------------------------------------------

# WAP to place the all even number in before the all the odd number
# input : 8
# 10 98 3 33 12 22 21 11
# output : 10 98 12 22 3 33 21 11
# list = [10,98,3,33,12,22,21,11]
# even = []
# odd = []
# for i in list:
#     if i%2 == 0:
#         even.append(i)
#     else:
#         odd.append(i)
# print(even+odd)

# --------------------------------------------------------------------------------

# Stack
# import sys
# class Stack:
#   def __init__(self): #parameterized constructor
#     self.stacklist = [] #stack created
#     self.stackSize = stackSize
#   def isFull(self):
#       if len(self.stacklist) == self.stackSize:
#           return True
#       else:
#           return False
#   def push(self, value):
#     if self.isFull():
#       print("Stack is full")
#     else:
#       self.stacklist.append(value)
#       print(self.stacklist)
#   def displaystack(self):
#     print(self.stacklist)
#   def isEmpty(self):
#         if self.stacklist == []:
#                 return True
#         else:
#                 return False      
#   def pop(self):
#       if self.isEmpty():
#           return "Stack is empty"
#       else:
#           return self.stacklist.pop()
#   def deleteStack(self):
#       self.stacklist = None
#       return "stack is deleted"
#   def peek(self):
#       if self.isEmpty():
#           return "Stack is empty"
#       else:
#           return self.stacklist[-1]
# size = int(input("enter the size of stack :"))
# stackobj = Stack(size)
# while True:
#   print("1. push element in stack :")
#   print("2. display stack element :")
#   print("3.check isempty :")
#   print("4.pop operation :")
#   print("5.delete stack :")
#   print("6.peek operation :")
#   print("7. exit")
#   choice = int(input("enter your choice : "))
#   if choice == 1:
#     val = int(input("enter value for stack :"))
#     stackobj.push(val)
#   elif choice == 2:
#     stackobj.displaystack()
#   elif choice == 3:
#       print(stackobj.isEmpty())
#   elif choice == 4:
#       print(stackobj.pop())
#   elif choice == 5:
#       print(stackobj.deleteStack())
#   elif choice == 6:
#       print(stackobj.peek())
#   elif choice == 7:
#       sys.exit()

# --------------------------------------------------------------------------------

# Tower of Hanoi
# rules 
# we can move only one disk at a time
# we have to pick upper disk from any one pipe 
# we have to place on top of any disk
# we can not place any large disk on top of smaller

# tower oh hanoi
import time

class TowerOfHanoi:
    def __init__(self, source):
        self.A = source[:]  # source rod
        self.B = []         # auxiliary rod
        self.C = []         # destination rod
        self.total_disks = len(source)
        self.step_count = 0

    # Display rods in aligned format
    def show_rods(self):
        print(f"A = {str(self.A):<12} B = {str(self.B):<12} C = {str(self.C):<12}")
        print("-" * 45)
        time.sleep(1)

    # Move disk between two rods
    def move(self, from_list, to_list):
        if not from_list:
            from_list.append(to_list.pop())
        elif not to_list:
            to_list.append(from_list.pop())
        elif from_list[-1] > to_list[-1]:
            from_list.append(to_list.pop())
        else:
            to_list.append(from_list.pop())

        self.step_count += 1
        self.show_rods()
        print(f"Pass {self.step_count} complete\n")
        print("---------------------------------------------")

    # Solve iteratively
    def solve_iteratively(self):
        print("Initial State:")
        self.show_rods()

        # Determine movement pattern based on even/odd number of disks
        if self.total_disks % 2 == 0:
            move1 = (self.A, self.B)
            move2 = (self.A, self.C)
            move3 = (self.B, self.C)
        else:
            move1 = (self.A, self.C)
            move2 = (self.A, self.B)
            move3 = (self.B, self.C)

        total_moves = 2 ** self.total_disks - 1

        for step in range(1, total_moves + 1):
            if step % 3 == 1:
                self.move(*move1)
            elif step % 3 == 2:
                self.move(*move2)
            else:
                self.move(*move3)

        print("All passes complete. Final State:")
        self.show_rods()


# Run
hanoi = TowerOfHanoi([3, 2, 1])
hanoi.solve_iteratively()