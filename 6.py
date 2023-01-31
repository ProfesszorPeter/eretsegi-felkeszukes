num1 = int(input("Add meg az első számot: "))
num2 = int(input("Add meg a második számot: "))
num3 = int(input("Add meg a harmadik számot: "))

if num1 < num2 and num1 < num3:
    print(num1)
elif num2 < num1 and num2 < num3:
    print(num2)
else:
    print(num3)