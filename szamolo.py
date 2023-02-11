import random

valasz = int(input("Milyen műveletet szeretne gyakorolni? \n \n 1.Összeadás \n 2. Kivonás\n 3. Szorzás \n Választás (1-3): "))

db = 0
ok = 0

for db in range (5):
    db +=1
    a = random.randint(1,10)
    b = random.randint(1,10)

    if valasz == 1:
        c = int(input(f"{a} + {b} = "))
        d = a + b

        if c == d:
            ok +=1
            print("Helyes!")
        else:
            print("Hibás!")

    elif valasz == 2:
        c = int(input(f"{a} - {b} = "))
        d = a - b
        
        if c == d:
            ok +=1
            print("Helyes!")
        else:
            print("Hibás!")
    else:
        c = int(input(f"{a} * {b} = "))
        d = a * b

        if c == d:
            ok +=1
            print("Helyes!")
        else:
            print("Hibás!")

print(f"Gratulálunk! \n Sikerült {ok} helyes műveletet elvégeznie {db} próbálkozásból.")