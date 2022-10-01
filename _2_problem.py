# Write a Python program to triple all numbers of a given list of integers. Use Python map.

size = int(input("Enter the size of eliment : "))
lst = []

for i in range(size):
    element = int(input("enter the value : "))
    lst.append(element)

print("list : ",lst)

res = list(map(lambda lst:lst*3,lst))
print("Triple of list numbers :",res)