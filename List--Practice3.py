# WAP to check if the number is present in the list or not.
# If the number is present, print the position of the number.
# Print the appropriate message if the number is not present in the list.
n=int(input("Enter the number of elements you want in the list: "))
l1=[]
for i in range(n):
    num=int(input("Enter the number: "))
    l1.append(num)
print("The list is: ",l1)
x=int(input("Enter the number you want to check: "))
if x in l1:
    print("The number is present in the list")
    print("The position of that number in the list is: ")
    for j in range(len(l1)):
        if l1[j] == x:
            print(j+1, end=" ")
else:
    print("The number is not present in the list")