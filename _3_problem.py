# Write a Python program to square the elements of a list using map() function.

size = int(input("enter the element size :"))
lst = []

for i in range(size):
    element = int(input("enter the value :"))
    lst.append(element)
print("list :",lst)

res = list(map(lambda lst : lst**2,lst))
print(res)
