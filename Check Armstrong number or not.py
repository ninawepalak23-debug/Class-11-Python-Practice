a=int(input("Enter hundredth place digit: "))
b=int(input("Enter tens place digit: "))
c=int(input("Enter ones place digit: "))
print("The number is: ", (a*100)+(b*10)+(c))
if (a**3)+(b**3)+(c**3)==(a*100)+(b*10)+(c):
    print("It is a Armstrong Number")
else:
    print("Not a Armstrong Number")