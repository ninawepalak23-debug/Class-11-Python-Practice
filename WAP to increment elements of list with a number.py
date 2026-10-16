n=int(input("Enter the number of elements you want to add: "))
l1=[]
l2=[]
#Program to make a list
for i in range(0,n):
    num=int(input("Enter the number: "))
    l1.append(num)
print("Original list is: ",l1)
# Program to increment the number taken from user in each..
# ..element of the list
n1=int(input("Enter the number which you want to increment in elements : "))
for i in range(n):
    n2=l1[i]
    n3=int(n2)+n1
    l2.append(n3)
print("New list is: ",l2)