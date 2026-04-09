# A company has a sales record of N products for M days. The company wishes to know the maximum revenue received from a given product of the N products each day. Write an algorithm to find the highest revenue received each day
# input : The first line of the input consist of two space-separatedintegers-days(M) and products(N), represnting the days and the products in the sales record. the next M lines consist of N spaces-separated integers representing the sales revenue received from each product each day
# input : [100,198,333,332][122,232,221,111][323,565,245,764]
#outout : 332 221 764
# Code :

# M = int(input("Enter number of days: "))
# N = int(input("Enter number of products: "))

# result = []

# print("Enter revenue data (each day in one line):")

# for i in range(M):
#     while True:
#         row = list(map(int, input(f"Day {i+1}: ").split()))
        
#         # Strict validation (important)
#         if len(row) != N:
#             print(f"Error: Enter exactly {N} values.")
#         else:
#             break

#     # Find max manually (no shortcuts)
#     max_val = row[0]
#     for j in range(1, N):
#         if row[j] > max_val:
#             max_val = row[j]

#     result.append(max_val)

# # Output
# print("Maximum revenue each day:")
# print(*result)

#=========================================================================================

# import sys

# class node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class  LinkedList:
#     def __init__(self):
#         self.head = None

#     def addnode(self, value):
#         new_node = node(value)
#         if self.head is None:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             self.tail.next = new_node
#             self.tail = new_node
    
#     def addNodeinBeginning(self, value):
#         new_node = node(value)
#         if self.head is None:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             new_node.next = self.head
#             self.head = new_node

#     def addNodeinBetween(self, value, left_value, right_value):
#         if self.head is None:
#             print("List is empty. Cannot insert between nodes.")
#             return

#         current = self.head
#         while current is not None:
#             if current.data == left_value and current.next is not None and current.next.data == right_value:
#                 new_node = node(value)
#                 new_node.next = current.next
#                 current.next = new_node
#                 if current is self.tail:
#                     self.tail = new_node
#                 return
#             current = current.next

#         print(f"No adjacent nodes found with values {left_value} and {right_value}. Cannot insert {value} between them.")

#     def addNodeatEnd(self, value):
#         new_node = node(value)
#         if self.head is None:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             self.tail.next = new_node
#             self.tail = new_node
    
#     def deleteNode(self, value):
#         current = self.head
#         prev = None
#         while current is not None:
#             if current.data == value:
#                 if prev is None:
#                     self.head = current.next
#                 else:
#                     prev.next = current.next
#                 if current is self.tail:
#                     self.tail = prev
#                 return
#             prev = current
#             current = current.next
#         print(f"Node with value {value} not found in the linked list.")

#     def searchNode(self, value):
#         current = self.head
#         while current is not None:
#             if current.data == value:
#                 return True
#             current = current.next
#         return False
    

#     def display(self):
#         current = self.head
#         while current is not None:
#             print(current.data, end=" -> ")
#             current = current.next
#         print("None")

#     def exit(self):
#         sys.exit()

# if __name__ == "__main__":
#     obj = LinkedList()

#     while True:
#         print("\n1. Add Node in Linked List :")
#         print("2. Add node in Beginning :")
#         print("3. Add node Between  :")
#         print("4. Add node at End :")
#         print("5. Delete Node :")
#         print("6. Search Node :")
#         print("7. Display Linked List :")
#         print("8. Exit")
        
#         choice = int(input("Enter your choice : "))
        
#         if choice == 1:
#             val = int(input("Enter value for node : "))
#             obj.addnode(val)
#         elif choice == 2:
#             val = int(input("Enter value for node : "))
#             obj.addNodeinBeginning(val)
#         elif choice == 3:
#             val = int(input("Enter value for node : "))
#             left_val = int(input("Enter the value of the node before the new node: "))
#             right_val = int(input("Enter the value of the node after the new node: "))
#             obj.addNodeinBetween(val, left_val, right_val)
#             print("Element Added Successfully")
#         elif choice == 4:
#             val = int(input("Enter value for node : "))
#             obj.addNodeatEnd(val)
#         elif choice == 5:
#             val = int(input("Enter value for node : "))
#             obj.deleteNode(val)
#             print("Element Deleted Successfully")
#         elif choice == 6:
#             val = int(input("Enter value for node : "))
#             if obj.searchNode(val):
#                 print(f"Node with value {val} found in the linked list.")
#             else:
#                 print(f"Node with value {val} not found in the linked list.")
#         elif choice == 7:
#             obj.display()
#         elif choice == 8:
#             obj.exit()

#================================================================

# ip = [0, 0, 1, 2, 0, 3, 0, 4]
# while ip and ip[0] == 0:
#     ip.pop(0)
# ip = [0, 0, 1, 2, 0, 3, 0, 4]
# while ip and ip[0] == 0:
#     ip.pop(0)
# print(ip)

#================================================================

# Regular Expression
# applications of regular expression
# 1. used to develop a digital circuit
# 2. used to develop the compiler and interpreter
# 3. used to develop the communication protocols like TCP/IP
# 4. used to develop the validation logic
# 5. used to develop the pattern matching and searching application like ctrl+f

