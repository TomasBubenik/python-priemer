x=0
y=0

z=True
while z:
    a = int(input("Zadaj číslo:"))
    b = str(input("Chceš pokračovať?y/n:"))
    if (b == "n"):
        print ("Priemer tvojich čisiel je:",x/y)
    x=y+a
    y=x+a

