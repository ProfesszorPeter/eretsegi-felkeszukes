a = int(input("Adja meg a háromszög egyik oldalát: "))
b = int(input("Adja meg a háromszög másik oldalát:"))
c = int(input("Adja meg a háromszög harmadik oldalát : "))

if a + b >= c and a + c >= b and b + c >= a :
    print("A háromszög megszekeszthető")
else:
    print("A háromszög nem szerkeszthető meg")