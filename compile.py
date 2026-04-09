# import re
# count = 0
# pattern = re.compile("function")
# # print(pattern)
# matcher = pattern.finditer("function in python is defined by a def statement. python the function is a block of code that is used to perform a single, related action. functions are used to organize code into reusable blocks.")
# # print(matcher)
# for i in matcher:
#     count += 1
#     print(i.start(),"...",i.end(),"...",i.group())
# print("The number of occurrences:",count)

#================================================================================

# import re
# count = 0
# matcher = re.finditer("python", "python is a programming language. python is used for web development. python is used for artificial intelligence. python is used for data science.")
# for i in matcher:
#     count += 1
#     print(i.start(),"...",i.end(),"...",i.group())
# print("The number of occurrences:",count)

#================================================================================

# import re 
# obj = input("Enter any character : ")
# objmatch=re.finditer(obj, "a7b,@92")
# #print(objmatch)
# for match in objmatch:
#     print(match.start(),"...",match.end(),"...",match.group())

#================================================================================

# Quantifiers
# match character classes
# match() function

# import re 
# a = input("Enter string to perform match operation :")
# atch = re.match(a,"Python is very important language")
# print(atch)
# if atch != None:
#     print("Ad")
#     print(atch.start(),"",atch.end())
# else:
#     print("There is no matching at beginning level")

#===============================================================================

# fullmatch() function
# as a name suggest wehn we have to match full string with the given pattern then we have to use this function if match is done then we will get match object otherwise we will get none
# import re 
# a = input("Enter string to perform match operation :")
# atch = re.fullmatch(a,"Python is very")
# print(atch)
# if atch != None:
#     print("Ad")
#     print(atch.start(),"",atch.end())
# else:
#     print("There is no matching at beginning level")

#===============================================================================

# search()function

# if the match found anywheere si the string then it return object else it will return none

# import re 
# a = input("Enter string to perform match operation :")
# atch = re.search(a,"Python is very important language")
# print(atch)
# if atch != None:
#     print("Ad")
#     print(atch.start(),"",atch.end(),atch.group())
# else:
#     print("There is no matching at beginning level")

#===============================================================================

# import re
# a = input("enter string:")
# f = open("myfile.txt", "r")
# c = f.read()
#    # define what you want to match
# mtch = re.search(a, c)
# print(mtch)
# if mtch != None:
#     print("match found")
#     print(mtch.start(), mtch.end())
# else:
#     print("match not found")
#===============================================================================

# findall()
# the funtion return a list which containing all the matches
# import re
# atch = re.findall("[0-9]","Aditya Thorat is Codder")
# print(atch)

#===============================================================================

# sub() function
# this funtion perform subtitution or replace operation
# re.sub(expression, replacement, string )here every match pattern will be replaced by the replacement string

# import re 
# obj = re.sub('[a-zA-Z]','x','Aditya Thorat')
# print(obj)

#===============================================================================

# subn()similar to sub diffrent is it return number of replacement
# import re
# obj = re.subn('[0-7]','@','asd987tr234@#$')
# print(obj)
# print("the string is = ",obj[0])
# print("the number of replacement is = ",obj[1])

#===============================================================================

# import re

# email = input("Enter email id: ")
# obj = re.fullmatch('[a-zA-Z0-9._]*@gmail[.]*.com', email)
# if obj != None:
#     print("Valid email id")
# else:
#     print("Invalid email id")

#===============================================================================
# import re

# mobile = input("Enter mobile number: ")
# obj = re.fullmatch('[0-9]\d{9}', mobile)
# if obj != None:
#     print("Valid mobile number")
# else:
#     print("Invalid mobile number")

#===============================================================================

# import os,sys
# fname = input("Enter file name:")
# if os.path.isfile(fname):
#     print("file exist:",fname)
#     f = open("fname",'r')
# else:
#     print("file dosen't exist",fname)
#     sys.exit(0)
# print("the content of file is:")
# data = f.read()
# print(data)