phy = float(input("Enter Physics marks: "))
chem = float(input("Enter Chemistry marks: "))
maths = float(input("Enter Maths marks: "))
gender = input("Enter Gender (m/f): ")
total = phy + chem + maths
percentage = total/3
print("Total Marks =", total)
print("Percentage =", percentage)
if percentage >= 60 and gender.lower() == "m":
    print("You are eligible for Placement")
else:
    print("You are eligible for Data Entry Job")