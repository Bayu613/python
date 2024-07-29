def persegi(s):
    keliling= 4 * s
    luas= s * s

    print("keliling persegi adalah", keliling)
    print("luas persegi adalah", luas)

def persegi_panjang(p, l):
    keliling=2*(p + l)
    luas= p * l

    print("keliling persegi panjang", keliling)
    print("luas persegi panjang", luas)

def jajar_genjang(a, b, c, d, t) :
    keliling = a + b + c + d 
    luas = a * t 

    print("keliling jajar genjang", keliling)
    print("luas jajar genjang", luas)

def lingkaran(r) :
    keliling = 2 * (22/7) * r 
    luas = (22/7) * r** 2

    print("keliling lingkaran", keliling)
    print("luas lingkaran", luas)

(pilihan) = int(input("masukkan pilihan anda 1,2,3,4 = "))

if(pilihan == 1):
    s = int(input("masukkan nilai s = "))
    persegi(s)
elif(pilihan == 2):
    p = int(input("masukkan nilai p = "))
    l = int(input("masukkan nilai l = "))
    persegi_panjang(p, l)
elif(pilihan == 3):
    a = int(input("masukkan nilai a = "))
    b = int(input("masukkan nilai b = "))
    c = int(input("masukkan nilai c = "))
    d = int(input("masukkan nilai d = "))
    t = int(input("masukkan nilai t = "))
    jajar_genjang(a, b, c, d, t)
elif(pilihan == 4):
    r = int(input("masukkan nilai r = "))
    lingkaran(r)
else :
    print("maaf pilihan anda tidak ada ")