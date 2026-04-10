# we use recursion especially in the cases we know that the problem can be divided into smaller sub problems.

# num = int(input("Enter a number: "))
# def poweroftwo(n):
#     if n == 0:
#         return 1
#     else:
#         power = poweroftwo(n-1)
#         return power * 2

# print(poweroftwo(num))

#===========================================================================================

# num = int(input("Enter a number: "))
# def powerofTwoIterative(n):
#     i = 0
#     power = 1
#     while i < n:
#         power = power * 2
#         i = i + 1
#     return power

# print(powerofTwoIterative(num))

#=============================================================================================

# def factorial(num):
#     if num <= 1:
#         return 1
#     else:
#         return num * factorial(num-1)
# print("4*3*2*1 = ",factorial(4))

#==============================================================================================

# def ispalindrome(string):
#     if len(string) == 0:
#         return True
#     if string[0] != string[-1]:
#         return False
#     return ispalindrome(string[1:-1])

# print(ispalindrome("aditya"))
# print(ispalindrome("subhash"))
# print(ispalindrome("thorat"))

#===============================================================================================

# def power(base, exponent):
#     if exponent == 0:
#         return 1
#     else:
#         return base * power(base, exponent-1)
# print(power(2,0))
# print(power(2,2))
# print(power(2,4))

#===============================================================================================

# def capitallizedfirst(arr):
#     result = []
#     if len(arr) == 0:
#         return result
#     else:
#         result.append(arr[0].upper() + arr[0][1:])
#         return result + capitallizedfirst(arr[1:])

# print(capitallizedfirst(["aditya","subhash","thorat"]))

#===============================================================================================

# def productofarray(arr):
#     if len(arr) == 0:
#         return 1
#     else:
#         return arr[0] * productofarray(arr[1:])
    
# print(productofarray([1,2,3]))
# print(productofarray([1,2,3,10]))

#===============================================================================================

# def fib(num):
#     if (num < 2):
#         return num
#     else:
#         return fib(num-1) + fib(num-2)
    
# print(fib(4))
# print(fib(10))
# print(fib(28))
# print(fib(35))
# # 0 1 1 2 3 5 

#===============================================================================================

# class Tree:
#     def __init__(self,data):
#         self.data = data
#         self.children = []

#     def addChild(self,child):
#         self.children.append(child)

#     def __str__(self,level=0):
#         ret = " "*level + str(self.data) + "\n"
#         for child in self.children:
#             ret += child.__str__(level+1)
#         return ret

# rootNode = Tree("Drinks")
# hot           = Tree("Hot")
# cold          = Tree("Cold")
# tea           = Tree("Tea")
# coffee        = Tree("Coffee")
# non_alcoholic = Tree("Non-Alcoholic")
# alcoholic     = Tree("Alcoholic")

# rootNode.addChild(hot)
# rootNode.addChild(cold)
# hot.addChild(tea)
# hot.addChild(coffee)
# cold.addChild(non_alcoholic)
# cold.addChild(alcoholic)

# print(rootNode)

#===============================================================================================

# full binary tree
# Each node has either 0 or 2 children
# no node has a single childe

#===============================================================================================

# complete binary tree
# all levels except possibly the last are completely filled
# nodes in the last level are filled from left to right

#===============================================================================================

# perfect binary tree
# all internet nodes have exactly two nodes
# all leaf nodes are at the same level

#===============================================================================================

# class Tree:
#     def __init__(self,data):
#         self.data = data
#         self.children = []

#     def addChild(self,child):
#         self.children.append(child)

#     def __str__(self,level=0):
#         ret = " "*level + str(self.data) + "\n"
#         for child in self.children:
#             ret += child.__str__(level+1)
#         return ret

# rootNode = Tree("N1")
# N2   = Tree("N2")
# N3   = Tree("N3")
# N4   = Tree("N4")
# N5   = Tree("N5")
# N6   = Tree("N6")
# N7   = Tree("N7")
# N9   = Tree("N9")
# N10  = Tree("N10")
# rootNode.addChild(N2)
# rootNode.addChild(N3)
# N2.addChild(N4)
# N2.addChild(N5)
# N3.addChild(N6)
# N3.addChild(N7)
# N4.addChild(N9)
# N4.addChild(N10)

# print(rootNode)

# ===============================================================================================
# import Queuelinkedlist as queue
# class BSTnode:
#     def __init__(self,data):
#         self.data = data
#         self.leftchild = None
#         self.rightchild = None

# def insertnode(rootnode,nodevalue):
#     if rootnode.data == None:
#         rootnode.data = nodevalue
#     elif nodevalue <= rootnode.data:

class node:

    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
class BinaryTree:
    def __init__(self):
        self.root = None
    
    def insert(self,value):
        if self.root is None:
            self.root = Node(value)
        else:
            self.insertNode(self.root, value)

    def insertNode(self,rootNode,value):
        if value < rootNode.value:
            if rootNode.left is None:
                rootNode.left = Node(value)
            else:
                self.insertNode(rootNode.left,value)
        else:
            if rootNode.right is None:
                rootNode.right = Node(value)
            else:
                self.insertNode(rootNode.left,value)

btobj = BinaryTree()
btobj.insert(50)
btobj.insert(30)
btobj.insert(70)

print(btobj)
