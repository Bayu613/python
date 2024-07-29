def tabung(r, t):
    vol = (22/7) * r ** 2 * t
    luas_selimut = 2 * (22/7) * r * t
    luas_alas = (22/7) * r **2
    luas_permukaan = 2 * (22/7) * r * (r + t)

    print("volume tabung adalah", vol)
    print("luas selimut tabung adalah ", luas_selimut)
    print("luas alas tabung adalah ", luas_alas)
    print("luas permukaan tabung adalah ", luas_permukaan)

tabung(4,8)

 