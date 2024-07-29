bintang=int(input("masukkan jumlah bintang ="))

for x in range(bintang + 1) :
    for z in range(bintang-x,0,-1):
        print("   ", end="")
    for y in range(x):
        print(" * ", end="")
    for y in range(x):
        print(" * ", end="")
    print("")

for x in range(bintang, 0,-1) :
    for z in range(bintang-x,0,-1):
        print("   ", end="")
    for y in range(x):
        print(" * ", end="")
    for y in range(x):
        print(" * ", end="")
    print("")

