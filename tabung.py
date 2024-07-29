#input
r =int(input("masukkan jari jari tabung = "))
t =int(input("masukkan tinggi tabung = " ))

#proses perhitungan
vol = (22/7) * r ** 2 * t
luas_selimut = 2 * (22/7) * r * t
luas_alas = (22/7) * r **2
luas_permukaan = 2 * (22/7) * r * (r + t)

#output
vol = (22/7) * r ** 2 * t
luas_selimut = 2 * (22/7) * r * t
luas_alas = (22/7) * r **2
luas_permukaan = 2 * (22/7) * r * (r + t)

print("vol tabung dengan jari jari ", r," cm adalah", vol)
print("luas selimut tabung dengan jari jari ", r, " cm adalah ", luas_selimut)
print("luas alas tabung dengan jari jari ", r, " cm  adalah ", luas_alas)
print("luas permukaan tabung dengan jari jari ", r, " cm adalah ", luas_permukaan)