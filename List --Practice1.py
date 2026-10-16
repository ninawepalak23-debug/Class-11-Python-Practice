#Ask the user to enter a list containing numbers between 1 and 12.
# Then replace all the entries in the list that are greater than 10 with 10
l1=[]
n1=int(input("Enter number of elements of list: "))
print("Please Enter the number between 1 and 12")
for i in range(n1):
    n2=int(input("Enter number: "))
    l1.append(n2)
print("List is: ",l1)
for i in range(n1):
    n3=l1[i]
    if n3>10:
        l1.pop(i)
        l1.insert(i,10)
print("New List is: ",l1)