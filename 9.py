import math

a = int(input("Adja meg az 'a' együttgatót: "))
b = int(input("Adja meg a 'b' együtthatót: "))
c = int(input("Adja meg a 'c' együtthatót: "))

if math.sqrt(a) or math.sqrt(c) <=0:
    print("Ez az egyenlet nem megoldható")
else:
    print("Ennek az egyenletnek van megoldássa")