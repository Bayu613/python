bb=int(input("masukkan berat badan = "))
tinggi=float(input("masukkan tinggi badan cm = "))

tinggi = tinggi / 100

bmi = (bb/(tinggi **2))

print(bmi)

if(bmi < 18.5) :
    print("berat badan kurang proporsional")
elif(bmi >= 18.5 and bmi < 22.9) :
    print("berat badan ideal")
elif(bmi >= 23 and bmi > 29.9) :
    print("berat badan berlebih")
elif(bmi > 30) :
    print("obesitas")

