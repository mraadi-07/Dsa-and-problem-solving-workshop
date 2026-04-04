# mydict = {
#     101 : "Aditya",
#     102 : "Tejas",
#     "103" : "Satyarth",
#     "104" : "Rishabh",
#     101 : "Tejas",
#     102 : "Aditya"
# }
# print(mydict)

#wit h the help of key we have to print values
# a = mydict[102]
# print(a)

# replace the value of key 102 with "Pratik"
# mydict[102] = "Pratik"
# print(mydict)

# only print the key x=0,1
# for x in mydict:
#     print(x)

# only print the values
# for x in mydict.values():
#    print(x)

# printing both key and value
# for x in mydict.items():
#   print(x)

# if i have to ad new key value pair in my dictionary
# mydict["mobile No"] = 464646738
# print(mydict)

# a = {(1,2):1,(2,3):2,(4,5):3}
# print(a[(4,5)])

# a = {'a':1,'b':2,'c':3}
# print(a['a','b'])

# arr = {}
# arr[1] = 1
# arr['1'] = 2
# arr[1] +=  1
# print(arr)
# sum = 0
# for k in arr:
#     sum += arr[k]
# print(sum)

# my_dist = {}
# my_dist[1] = 1
# my_dist['1'] = 2
# my_dist[1.0] = 4
# sum = 0
# for k in my_dist:
#     sum += my_dist[k]
# print(sum)

# my_dist = {}
# my_dist[(1,2,4)] = 8
# my_dist[(4,2,1)] = 10
# my_dist[(1,2)] = 12
# sum = 0
# for k in my_dist:
#     sum += my_dist[k]
# print(sum)
# print(my_dist)

# box = {}
# jars = {}
# crates = {}
# box['Biscuit'] = 1
# box['cake'] = 3
# jars['jam'] = 4
# crates['box'] = box
# crates['jars'] = jars
# print(len(crates[box]))

# dist = {'c': 97, 'a': 96, 'b':98}
# for _ in sorted(dist):
#     print(dist[_])

# rec = {"Name" : "python", "Age":"20"}
# r = rec.copy()
# print(id(r) == id(rec))
# print(id(r))
# print(id(rec))

# rec = {"name":"Python","age":20,"Addr":"New York"}
# id1 = id(rec)
# del rec
# rec = {"name":"Python","age":20,"Addr":"New York"}
# id2 = id(rec)
# print(id1 == id2)
# print(id1)
# print(id2)

# logic : iterate through the dictionary and keep track of the key with the minimun value 
# input : {"X":20, "Y":10, "Z":30}
# output : "Y"
# ip = {"x":20,"y":10,"z":30 }
# op = min(ip.values())
# print(op)

