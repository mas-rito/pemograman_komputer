def persegi():
    sisi = float(input("Masukkan panjang sisi: "))
    luas = sisi * sisi
    return luas

def persegi_panjang():
    panjang = float(input("Masukkan panjang: "))
    lebar = float(input("Masukkan lebar: "))
    luas = panjang * lebar
    return luas

def segitiga():
    alas = float(input("Masukkan alas: "))
    tinggi = float(input("Masukkan tinggi: "))
    luas = (alas * tinggi) / 2
    return luas

def lingkaran():
    jari_jari = float(input("Masukkan jari-jari: "))
    luas = 3.14 * jari_jari * jari_jari
    return luas

def luas_bangun_datar():
    print('=======================')
    print("Pilih bangun datar:")
    print("1. Persegi")
    print("2. Persegi Panjang")
    print("3. Segitiga")
    print("4. Lingkaran")
    pilihan_bangun = int(input("Masukkan pilihan Anda: "))
    print('=======================')

    if pilihan_bangun == 1:
        luas = persegi()
        print("Luas persegi:", luas)
    elif pilihan_bangun == 2:
        luas = persegi_panjang()
        print("Luas persegi panjang:", luas)
    elif pilihan_bangun == 3:
        luas = segitiga()
        print("Luas segitiga:", luas)
    elif pilihan_bangun == 4:
        luas = lingkaran()
        print("Luas lingkaran:", luas)
    else:
        print("Pilihan tidak valid.")
    print('=======================')
    