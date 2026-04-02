ch = ord(input("Enter any character :"))
#ord fumvtion used to convert in ASCIT code 
if ch >= 65 and ch <= 91:
    print("Uppercase")
elif ch >= 97 and ch <= 122:
    print("Lowercase")
elif ch >= 48 and ch <= 57:
    print("Digit")
else:
    print("your enterd character is in special symbols")