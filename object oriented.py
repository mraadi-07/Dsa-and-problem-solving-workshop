# class student:

#     roll_no = 101 # data member
    
#     def studentData(self): # method/ member funtion
#         print("Student Information")

# obj = student()
# print(obj.roll_no)
# obj.studentData()

#---------------------------------------------------------

# constuctor
# class Demo:
#     def __init__(self):
#         print("I am  a constructor")
    
#     def msg(self):
#         print("Hello Class")
# obj = Demo()
# # print(obj)
# obj1 = Demo()
# obj.msg()

#------------------------------------------------------------

# class Hod:
#     def __init__(self):
#         self.name = "Aditya"
#         self.age = 24
#         self.emp_id = 101
#     def info(self):
#             print("My name is",self.name)
#             print("My age is",self.age)
#             print("My emp id is",self.emp_id)
# obj = Hod()
# obj.info()

#------------------------------------------------------------   
# class Hod:
#     def __init__(self,name,age,empid):
#         self.name= name
#         self.age=age
#         self.empid=empid

#     def show(self):
#         print("My name is",self.name)
#         print("My age is",self.age)
#         print("My emp id is",self.empid)
# obj = Hod("aditya",7,101)
# obj.show()

#------------------------------------------------------------

# class New:
#     def __init__(self):
#         self.a = 10

# obj1 = New()
# obj2 = New()
# obj3 = New()
# print(obj1.a)
# print(obj2.a)
# print(obj3.a)
# obj1.a = 20
# print()
# print(obj1.a)
# print(obj2.a)
# print(obj3.a)

#------------------------------------------------------------

# class Student:
#     def __init__(self):
#         self.s_name = "Aditya"
#         self.s_rollno = 101
#     def getdata(self):
#         self.s_mb = 1234567890 #declaring a isinstance var inside a isinstance method

# obj = Student()
# obj.getdata()
# del obj.s_mb
# obj.s_branch = "CSE"
# print(obj.__dict__)

#------------------------------------------------------------

# class New:
#     a = 10
#     def __init__(self):
#         self.name = "Aditya"

# obj1 = New()
# obj2 = New()
# obj3 = New()
# print(obj1.a)
# print(obj2.a)
# print(obj3.a)
# New.a = 50
# print(obj1.a)
# print(obj2.a)    
# print(obj3.a)    

#------------------------------------------------------------

# Create a table with studentID, studentrollno, studentname and studentcity
# Add student
# Delete student
# Update student

#------------------------------------------------------------


# WAP to implement CRUD operations for a student management system using classes in Python.
# import sys

# class CRUD:
#     def __init__(self):
#         print("Welcome to Student Management System")
#         self.studentID = []
#         self.studentName = []
#         self.studentRollNo = []
#         self.studentCity = []
        
#     def addStudent(self):
#         self.studentID.append(int(input("Enter student ID: ")))
#         self.studentName.append(input("Enter student name: "))
#         self.studentRollNo.append(int(input("Enter student roll number: ")))
#         self.studentCity.append(input("Enter student city: "))
        
#     def viewStudent(self):
#         for i in range(len(self.studentID)):
#             print(f"ID: {self.studentID[i]}, Name: {self.studentName[i]}, Roll No: {self.studentRollNo[i]}, City: {self.studentCity[i]}")
    
#     def updateStudent(self):
#         id = int(input("Enter student ID to update:"))
#         if id in self.studentID:
#             index = self.studentID.index(id)
#             self.studentName[index] = input("Enter new name: ")
#             self.studentRollNo[index] = int(input("Enter new roll number: "))
#             self.studentCity[index] = input("Enter new city: ")
#         else:
#             print("Student ID not found.")
            
#     def deleteStudent(self):
#         id = int(input("Enter student ID to delete:"))
#         if id in self.studentID:
#             index = self.studentID.index(id)
#             del self.studentID[index]
#             del self.studentName[index]
#             del self.studentRollNo[index]
#             del self.studentCity[index]
#         else:
#             print("Student ID not found.")
            
# crud = CRUD()
# while True:
#     print("1. Add Student")
#     print("2. View Students")
#     print("3. Update Student")
#     print("4. Delete Student")
#     print("5. Exit")
    
#     choice = int(input("Enter your choice: "))
    
#     if choice == 1:
#         crud.addStudent()
#     elif choice == 2:
#         crud.viewStudent()
#     elif choice == 3:
#         crud.updateStudent()
#     elif choice == 4:
#         crud.deleteStudent()
#     elif choice == 5:
#         print("Exiting...")
#         sys.exit()
#     else:
#         print("Invalid choice. Please try again.")

#------------------------------------------------------------

# class Student:
#     def __init__(self,name,roll_no,mob):
#         self.name = name
#         self.roll_no = roll_no
#         self.mob =mob
#     def display(self):
#         print(self.name,"",self.roll_no,"",self.mob)
# stud = Student("Aditya",101,984916143)
# stud.display()

#------------------------------------------------------------

# class Student:
#     @staticmethod
#     def get_personal_detail(firstname, lastname):
#         print("Your personal Detail",firstname,lastname)
#     @staticmethod
#     def constant_detail(mobile_no, roll_no):
#         print("Your Constant Detail",mobile_no,roll_no)

# Student.get_personal_detail("Aditya","thorat")
# Student.constant_detail(984916143,101)

#------------------------------------------------------------

