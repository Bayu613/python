def kategori_curah_hujan(CH) :
    if( CH > 100 ) :
        print("sangat lebat")
    elif( CH < 100 and CH >= 50 ) :
        print("lebat")

CH = int(input("masukkan nilai CH = "))
kategori_curah_hujan(CH)