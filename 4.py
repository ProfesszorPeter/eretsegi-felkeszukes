num1= int(input("Add meg az első számot:"))
num2= int(input("Add meg a második számot: "))

osszeg = num2 + num1
kulonbseg = num1 - num2
szorzat = num2 * num1
#hanyados = num1 / num2

print(osszeg)
print(kulonbseg)
print(szorzat)
#print(hanyados)

#hanyados
if num1 % num2 == 0:
    print(num1 / num2)
else:
    exit 

#def hanyados:
#    if num1 % num2 == 0:
#        print(hanyados)