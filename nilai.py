# jika nilai > 90 maka grade A
# jika nilai 80> maka grade B
# jika nilai 70> maka grade C
# jika nilai 60> maka grade D

nilai= (int(input("masukkan nilai = ")))
if(nilai > 90 and nilai <= 100) :
    print("GRADE A")
elif(nilai > 80 and nilai <= 90) :
    print("GRADE B") 
elif(nilai > 70 and nilai <= 80) :
    print("GRADE C")
elif(nilai > 60 and nilai <= 70) :
    print("GRADE D") 
elif(nilai >= 0 and nilai <= 60) :
    print("GRADE E")
elif(nilai <= 100 or nilai >= 0) :
    print("TIDAK VALID")