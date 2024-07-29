def kubus(rusuk):
    luas = 6 * r**2
    volume = r ** 3

    print("luas kubus", luas)
    print("vol kubus", volume)

def balok(p, l, t):
    luas = 2 * (p * l) + (p * t) + (l + t)
    volume = (p * l * t)

    print("luas balok", luas)
    print("vol balok", volume)

(pilihan) = int(input("masukkan pilihan anda 1,2 ="))

if ( pilihan == 1 ):
    r = int(input("masukkan rusuk kubus = "))
    kubus(r)
elif( pilihan == 2) :
    p = int(input("masukkan panjang balok = "))
    l = int(input("masukkan lebar balok = "))
    t = int(input("masukkan tinggi balok = "))

    balok(p,l,t)
else :
    print("maaf pilihan anda tidak ada")