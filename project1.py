# soal no 17
def pythagoras(a, b):
    c = (a ** 2 + b ** 2) ** (0.5)
    print ("nilai c adalah ", c)
# soal nomor 18
def kategorikan_sudut(sudut_c) :
    if sudut_c < 90 :
        print("segitiga tumpul")
    elif sudut_c == 90 :
        print("segitiga siku-siku")
    else:
        print("segitiga lancip")
# soal nomor 1
def mean(jumlah_data,banyak_data) :
    mean = jumlah_data / banyak_data 
    print(f"hasil mean dari jumlah data {jumlah_data} dan banyaknya data {banyak_data} adalah {mean}")

def median(data):
    if hitung_data % 2 == 1 :
        median = data[hitung_data // 2]
    else :
        median = (data[(hitung_data // 2) - 1] + data[hitung_data // 2]) / 2
    print("median dari data di atas adalah = ", median)
        
# soal nomor 4
def gaya_coulomb(k, q1, q2, r) :
    f = k * q1 * q2 / r **2
    print(f)
# soal nomor 7
def perubahan_energi_panas(m,c,t) :
    Q = m * c * t
    print(Q)
# soal nomor 6
def suhu_kalor_pemuaian(m, delta_v) :
    w = 0.5 * m * delta_v **2
    print(w)
# soal nomor 3
def seri(r1,r2,r3,r4) :
    Rtotal = r1 + r2 + r3 + r4
    print(Rtotal)
def paralel(r1,r2) :
    Rtotal = r1 * r2 /  r1 + r2
    print(Rtotal)
# soal nomor 12
def daya(w,t) :
    p = w / t 
    print(p)
def energi_kinetic(m,v) :
    Ek = 0.5 * m * v **2
    print(Ek)
# soal nomor 13
def cepat_rambat(lamda,t) : 
    v = lamda / t 
    print(v)
def tekanan(f,a) :
    p = f / a 
    print(p)

def konversi_suhu(celcius,farenheit,kelvin,reamur) :
    c_ke_f = (celcius * 9/5) + 32
    c_ke_k = celcius + 273.15
    c_ke_r = 4/5 * celcius
    f_ke_c = (f - 32) * 5/9
    F_ke_k = (f - 32) * 5/9 + 273.15
    f_ke_r = (f - 32) * 4/9
    k_ke_c = k - 273.15
    k_ke_f = (k - 273.15) * 9/5 + 32
    k_ke_r = (k - 273.15) * 4/5
    r_ke_c = r * 5/4
    r_ke_f = (r * 9/4) + 32
    r_ke_k = (r * 5/4) + 273.15
    print("_"*55)
    print("celcius ke fanrenheit adalah",c_ke_f,"fanrenheit")
    print("celcius ke kalvin adalah",c_ke_k,"kelvin")
    print("celcius ke reamur adalah",c_ke_r,"reamur")
    print("_"*55)
    print("fanrenheit ke celcius adalah",f_ke_c,"celcius")
    print("fanrenheit ke kelvin adalah",F_ke_k,"kelvin")
    print("fanrenheit ke reamur adalah",f_ke_r,"reamur")
    print("_"*55)
    print("kelvin ke celcius adalah",k_ke_c,"celcius")
    print("kelvin ke fanrenheit adalah",k_ke_f,"fanrenheit")
    print("kelvin ke reamur adalah",k_ke_r,"reamur")
    print("_"*55)
    print("reamur ke celcius adalah",r_ke_c,"celcius")
    print("reamur ke fanrenheit adalah",r_ke_f,"fanrenheit")
    print("reamur ke kelvin adalah",r_ke_k,"kelvin")
#soal nomor 21
def bola(r) :
    luas = 4 * (22/7) * r**2
    volume = (4/3) * (22/7) * r **3

    print("luas bola",luas)
    print("volume bola",volume)   
def kerucut(r,t,s) :
    luas = ((22/7) * r **2) + ((22/7) * r * s)
    volume = (1/3) * (22/7) * r **2 * t 

    print("luas kerucut",luas)
    print("volume kerucut",volume)
def prisma_segitiga(a,t,b,c,d,tp) :
    luas = 2 * (1/2 * a * t) + (b + c + d) * tp   
    volume = (1/2 * a * t) * tp

    print("luas prisma segitiga",luas)
    print("volume prisma segitiga",volume)
def masa_jenis(m,v) :
    row = m / v 
    print("masa jenis nya adalah", row)
def kecepatan(s,t) :
    v = s / t 
    print("kecepatannya adalah", v)
def tekanan(row,q,h) :
    p = row * q * h 
    print("nilai p adalah ",p)
def gaya_apung(p,v,q) :
    f = p * v * q 
    print("nilai f adalah ", f)
# soal nomor 10
def gaya(m,a) :
    f = m * a 
    print("nilai f adalah ",f)
def usaha(s,t) :
    v = s / t 
    print("nilai v adalah ", v)
# soal nomor 9
def energi_potensial(m,g,h) :
    Ep = m * g * h 
    print("nilai energi potensialnya adalah", Ep)
def energi_mekanik(Ek,Em) :
    mekanik = Ek + Em 
    print("nilai energi mekaniknya adalah ", mekanik)

while True : 
    menu = int(input("\nmasukkan pilihan = \n 1. Teorema Pythagoras\n 2. mengkategorikan sudut segitiga siku siku c\n 3. mean median\n 4. Gaya coulumb\n 5. perubahan energi panas\n 6. suhu kalor dan pemuaian\n 7. rangkaian resistor paralel dan seri\n 8. daya\n 9. cepat rambat dan tekanan\n 10. konversi suhu\n 11. bangun ruang\n 12. masa jenis dan kecepatan\n 13. Tekanan dan Gaya apung\n 14. gaya dan usaha\n 15. energi potensial dan energi mekanik\n masukkan pilihan anda = "))
    
    if menu == 1 :
        a = int(input("masukkan nilai a = "))
        b = int(input("masukkan nilai b = "))
        pythagoras(a, b)

    elif menu == 2 :
        a = float(input("masukkan panjang sisi a = "))
        b = float(input("masukkan panjang sisi b = "))
        sudut_c = (a**2 + b**2) **0.5
        print(a)
        print(b)
        sudut_c_red = a / b 
        sudut_c_deg = sudut_c_red
        print('sudut c ====' + str(sudut_c_deg))

        print("sudut c adalah", sudut_c_deg, "derajat :")
        kategorikan_sudut(sudut_c)
        
    elif menu == 3 :
        print("1. mean")
        print("2. median")
        pilihan = int(input("masukkan pilihan anda 1,2 = "))
        if pilihan == 1 :
            jumlah_data = int(input("masukkan jumlah data = "))
            banyak_data = int(input("masukkan banyaknya data = "))
            mean(jumlah_data,banyak_data)
        elif pilihan == 2 :
            data = [6,7,5,6,9,8,4,9,8]
            data.sort ()
            hitung_data = len(data)
            print(data)
            median(data)
        else :
            print("maaf pilihan anda tidak ada")

    elif menu == 4 :
        k = 9 * 10^9
        q1 = int(input("masukkan nilai q1 = "))
        q2 = int(input("masukkan nilai q2 = "))
        r = int(input("masukkan nilai r = "))
        gaya_coulomb(k, q1, q2, r)

    elif menu == 5 : 
        m = int(input("masukkan nilai m = "))
        c = int(input("masukkan nilai c = "))
        t = int(input("masukkan nilai t = "))
        perubahan_energi_panas(m,c,t)
    
    elif menu == 6 :
        m = int(input("masukkan nilai m ="))
        delta_v = int(input("masukkan nilai delta_v ="))
        suhu_kalor_pemuaian(m, delta_v)

    elif menu == 7 :
        (pilihan) = int(input("masukkan pilihan anda 1,2 = "))
        if pilihan == 1 :
            r1 = int(input("masukkan r1 seri = "))
            r2 = int(input("masukkan r2 seri = "))
            r3 = int(input("masukkan r3 seri = "))
            r4 = int(input("masukkan r4 seri = "))
            seri(r1, r2, r3, r4)
        elif pilihan == 2 :
            r1 = int(input("masukkan r1 paralel = "))
            r2 = int(input("masukkan r2 paralel = "))
            paralel (r1, r2)
        else :
            print("maaf pilihan anda tidak ada")
    
    elif menu == 8 :
        (pilihan) = int(input("masukkan pilihan anda 1,2 = "))
        if pilihan == 1 :
            w = int(input("masukkan nilai w = "))
            t = int(input("masukkan nilai t = "))
            daya(w,t)
        elif pilihan == 2 :
            m = int(input("masukkan nilai m = "))
            v = int(input("masukkan nilai v = "))
            energi_kinetic(m,v)
        else :
            print("maaf pilihan anda tidak ada")
    
    elif menu == 9 :
        (pilihan) = int(input("masukkan pilihan anda 1,2 = "))
        if pilihan == 1 :
            def cepat_rambat(lamda,t) : 
                v = lamda / t 
                print(v)
            lamda = int(input("masukkan nilai lamda = "))
            t = int(input("masukkan nilai t = "))
            cepat_rambat(lamda,t)
        elif pilihan == 2 :
            def tekanan(f,a) :
                p = f / a 
                print(p)
            f = int(input("masukkan nilai f = "))
            a = int(input("masukkan nilai a = "))
            tekanan(f,a)
        else :
            print("maaf pilihan anda tidak ada")

    elif menu == 10 : 
        if konversi_suhu :
            celcius = float(input("masukkan celcius = "))
            f = float(input("masukkan fanrenheit = "))
            k = float(input("masukkan kelvin = "))
            r = float(input("masukkan reamur = "))
            konversi_suhu(celcius,f,k,r)

    elif menu == 11 :
        (pilihan) = int(input("masukkan pilihan anda 1,2,3 = "))
        if (pilihan == 1 ) :
            r = int(input("masukkan nilai r = "))
            bola(r)
        elif (pilihan == 2 ) :
            r = int(input("masukkan nilai r = "))
            t = int(input("masukkan nilai t = "))
            s = int(input("masukkan nilai s = "))
            kerucut(r,t,s)
        elif (pilihan == 3 ) :
            a = int(input("masukkan nilai a = "))
            t = int(input("masukkan nilai t = "))
            b = int(input("masukkan nilai b = "))
            c = int(input("masukkan nilai c = "))
            d = int(input("masukkan nilai d = "))
            tp = int(input("masukkan nilai tp = "))
            prisma_segitiga(a,t,b,c,d,tp)
        else :
            print("maaf pilihan anda tidak ada")

    elif menu == 12 : 
        print("1. masa jenis")
        print("2. kecepatan ")
        (pilihan) = int(input("masukkan pilihan anda 1,2 = "))
        if (pilihan == 1 ) :
            m = int(input("masukkan nilai m = "))
            v = int(input("masukkan nilai v = "))
            masa_jenis(m,v)
        elif (pilihan == 2 ) :
            s = int(input("masukkan nilai s = "))
            t = int(input("masukkan nilai t = "))
            kecepatan(s,t)
        else :
            print("maaf pilihan anda tidak ada")

    elif menu == 13 :
        print("1. tekanan")
        print("2. gaya apung")
        (pilihan) = int(input("masukkan pilihan anda 1,2 = "))
        if pilihan == 1 :
            row = int(input("masukkan nilai row = "))
            q = int(input("masukkan nilai q = "))
            h = int(input("masukkan nilai h = "))
            tekanan(row,q,h)
        elif pilihan == 2 :
            p = int(input("masukkan nilai p = "))
            v = int(input("masukkan nilai v = "))
            q = int(input("masukkan nilai q = "))
            gaya_apung(p,v,q)
        else :
            print("maaf pilihan anda tidak ada")

    elif menu == 14 : 
        print("1. gaya")
        print("2. usaha")
        (pilihan) = int(input("masukkan pilihan anda 1,2 = "))
        if pilihan == 1 :
            m = int(input("masukkan nilai m = "))
            a = int(input("masukkan nilai a = "))
            gaya(m,a)
        elif pilihan == 2 :
            s = int(input("masukkan nilai s = "))
            t = int(input("masukkan nilai t = "))
            usaha(s,t)
        else : 
            print("maaf pilihan anda tidak ada")

    elif menu == 15 :
        print("1. energi potensial")
        print("2. energi mekanik")
        (pilihan) = int(input("masukkan pilihan anda 1,2 = "))
        if pilihan == 1 :
            m = int(input("masukkan nilai m = "))
            g = int(input("masukkan nilai g = "))
            h = int(input("masukkan nilai h = "))
            energi_potensial(m,g,h)
        elif pilihan == 2 :
            Ek = int(input("masukkan nilai Ek = "))
            Em = int(input("masukkan nilai Em = "))
            energi_mekanik(Ek,Em)
        else : 
            print("maaf pilihan anda tidak ada")






    









