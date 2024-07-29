def sudut(a,b) :
    c = (a **2 + b**2) **(0.5)
    print("nilai sudut c adalah", c)

a = int(input("masukkan nilai a = "))
b = int(input("masukkkan nilai b = "))

if (c < 120 ) :
    print("Segitiga Tumpul")
elif (c == 90) :
    print("Segitiga siku siku")
elif (c < 90 and c ==> 30) :
    print("Segitiga Lancip")