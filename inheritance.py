# extracting property from one class to another class
# inheritance is used to reduce code
# by using inheritance we can reuse the code
#  Base class : A class which inherits its property from another class
# Derived class : A class in which properites are inherited
# types of inheritance
# 1. Single inheritance
# 2. Multiple inheritance
# 3. Multilevel inheritance
# 4. Hierarchical inheritance

# single inheritance
# class derived-class(base-class):

# class college:
#     def college_name(self):
#         print('college')

# class Student(college):
#     def student_info(self):
#         print('name: Aditya Thorat')
#         print('Branch: cse')
# obj = Student()
# obj.college_name()
# obj.student_info()

#------------------------------------------------------------

# Multilevel inheritance
# class grandfather
# ----------------
# class father(grandfather):
# ----------------
# class child(father):
# ----------------
# class college:
#     def college_name(self):
#         print('mordern college')

# class Student(college):
#     def student_info(self):
#         print('name: Aditya Thorat')
#         print('Branch: cs')

# class Exam(Student):
#     def subject(self):
#         print("subject1: define Engineering")
#         print("subject2: math")
#         print("subject3: c language")
# obj = Exam()
# obj.college_name()
# obj.student_info()
# obj.subject()

#-------------------------------------------------------------------

# Multiple inheritance

# class Submarks:
#     math = int(input("Enter math marks : "))
#     physics = int(input("Enter physics marks : "))
#     chemistry = int(input("Enter chemistry marks : "))
#     biology = int(input("Enter biology marks : "))
# #==================================== parent class
# class practicalMarks:
#     cpract = int(input("Enter c practical marks : "))
# #==================================== parent class2
# class Result(Submarks,practicalMarks):
#     #print("if student pass in both = subject and practical paper then pass")
#     def total(self):
#         if self.math >= 40 and self.physics >= 40 and self.chemistry >= 40 and self.biology >= 40 and self.cpract >= 40:
#             print("pass")
#         else:
#             print("fail")

# obj = Result()
# obj.total()

#-----------------------------------------------------------------

# Polymorphism


# class Principle:
#     def role(self):
#         print("I am managing all acivity of collage")

# class Deam:
#     def role(self):
#         print("I am decision taking person")
# class Hod:
#     def role(self):
#         print("I have responsibility to take decision")
# class faculty:
#     def role(self):
#         print("I am responsible for teaching")

# def func(obj):
#     obj.role()
# campus=[Principle(),Deam(),Hod(),faculty()]
# for obj in campus:
#     func(obj)

#---------------------------------------------------------------

# Overloading and Overriding
# #  python does not support method overloading and overriding
# Code :

# class Arithmetic:
#     def add(self,a):
#         print(a)
#     def add(self,a,b):
#         print(a+b)
#     def add(self,a,b,c):
#         print(a+b+c)
# obj = Arithmetic()
# obj.add(10)
# obj.add(10,20)
# obj.add(1,2,3)
 
#---------------------------------------------------------------

# class Arithmetic:
#     def add(self,a=None,b=None,c=None):
#       if a!=None and b==None and c==None:
#         print(a)
#       elif a!=None and b!=None and c==None:
#         print(a+b)
#       elif a!=None and b!=None and c!=None:
#         print(a+b+c)
# obj = Arithmetic()
# obj.add(10)
# obj.add(10,20)
# obj.add(1,2,3)

#---------------------------------------------------------------

# class Arithmetic:
#     def __init__(self):
#         print("There is no constructor ")
#     def __init__(self,a):
#         print("There is one constructor ")
#     def __init__(self,a,b):
#         print("There is twoconstructor ")
# obj = Arithmetic()
# obj = Arithmetic(10)
# obj = Arithmetic(1,2)

#---------------------------------------------------------------

# python supports both overriding  : 1. method overriding 2. constructor overriding
# method overriding(parent and child reatioship must be there)
# class RBI:
#     def home_loan(self):
#         print("home loan = 7.5")
    
#     def car_loan(self):
#         print("car loan = 8")
# class SBI(RBI):
#     def home_loan(self):
#         print(" SBI provide home loan = 6.5")
#         super().home_loan()# using super method you access the parent class method in child class
# obj = SBI()
# obj.home_loan() #child class method overrid the parent class method

#---------------------------------------------------------------

# class Father:
#     def __init__(self):
#         print("father")

# class Child(Father):
#     def __init__(self):
#         print("child")

# obj = Child()

#---------------------------------------------------------------

class Father:
    def __init__(self):
        print("father: i am already at breakfast table")

class Child(Father):
    def __init__(self):
        print("child:i will be late for breakfast")
        super().__init__()

obj = Child()

