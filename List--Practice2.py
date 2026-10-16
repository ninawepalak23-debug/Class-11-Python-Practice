# Ask the user to enter list of strings.
# Create a new list that consists of those strings with their first characters remoed
n=int(input("Enter the number of strings you want in list:"))
l1=[]
l2=[]
for i in range(0,n):
    string=input("Enter the string: ")
    l1.append(string)
print("The Original list is: ",l1)
for st in l1:
    str=st[1:len(st)]
    l2.append(str)
print("The New list is: ",l2)
