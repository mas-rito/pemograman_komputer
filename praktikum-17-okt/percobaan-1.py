# Buatlah program dalam bentuk fungsi menu, fungsi untuk mencari luas bangun datar  dan fungsi untuk mencari volume bangun ruang !

def menu():
    print("Menu Perhitungan Luas dan Volume")
    print("1. Hitung Luas Bangun Datar")
    print("2. Hitung Volume Bangun Ruang")
    print("3. Keluar")
    pilihan = int(input("Masukkan pilihan Anda: "))
    return pilihan

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
        sisi = float(input("Masukkan panjang sisi: "))
        luas = sisi * sisi
        print("Luas persegi:", luas)
    elif pilihan_bangun == 2:
        panjang = float(input("Masukkan panjang: "))
        lebar = float(input("Masukkan lebar: "))
        luas = panjang * lebar
        print("Luas persegi panjang:", luas)
    elif pilihan_bangun == 3:
        alas = float(input("Masukkan alas: "))
        tinggi = float(input("Masukkan tinggi: "))
        luas = (alas * tinggi) / 2
        print("Luas segitiga:", luas)
    elif pilihan_bangun == 4:
        jari_jari = float(input("Masukkan jari-jari: "))
        luas = 3.14 * jari_jari * jari_jari
        print("Luas lingkaran:", luas)
    else:
        print("Pilihan tidak valid.")
    print('=======================')
    

def volume_bangun_ruang():
    print('=======================')
    print("Pilih bangun ruang:")
    print("1. Kubus")
    print("2. Balok")
    print("3. Tabung")
    pilihan_bangun = int(input("Masukkan pilihan Anda: "))
    print('=======================')


    if pilihan_bangun == 1:
        sisi = float(input("Masukkan panjang sisi: "))
        volume = sisi * sisi * sisi
        print("Volume kubus:", volume)
    elif pilihan_bangun == 2:
        panjang = float(input("Masukkan panjang: "))
        lebar = float(input("Masukkan lebar: "))
        tinggi = float(input("Masukkan tinggi: "))
        volume = panjang * lebar * tinggi
        print("Volume balok:", volume)
    elif pilihan_bangun == 3:
        jari_jari = float(input("Masukkan jari-jari: "))
        tinggi = float(input("Masukkan tinggi: "))
        volume = 3.14 * jari_jari * jari_jari * tinggi
        print("Volume tabung:", volume)
    else:
        print("Pilihan tidak valid.")
    print('=======================')


while True:
    pilihan_utama = menu()

    if pilihan_utama == 1:
        luas_bangun_datar()
    elif pilihan_utama == 2:
        volume_bangun_ruang()
    elif pilihan_utama == 3:
        break
    else:
        print("Pilihan tidak valid.")
