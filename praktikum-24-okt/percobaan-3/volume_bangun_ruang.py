def kubus():
    sisi = float(input("Masukkan panjang sisi: "))
    volume = sisi * sisi * sisi
    return volume

def balok():
    panjang = float(input("Masukkan panjang: "))
    lebar = float(input("Masukkan lebar: "))
    tinggi = float(input("Masukkan tinggi: "))
    volume = panjang * lebar * tinggi
    return volume

def tabung():
    jari_jari = float(input("Masukkan jari-jari: "))
    tinggi = float(input("Masukkan tinggi: "))
    volume = 3.14 * jari_jari * jari_jari * tinggi
    return volume

def volume_bangun_ruang():
    print('=======================')
    print("Pilih bangun ruang:")
    print("1. Kubus")
    print("2. Balok")
    print("3. Tabung")
    pilihan_bangun = int(input("Masukkan pilihan Anda: "))
    print('=======================')


    if pilihan_bangun == 1:
        volume = kubus()
        print("Volume kubus:", volume)
    elif pilihan_bangun == 2:
        volume = balok()
        print("Volume balok:", volume)
    elif pilihan_bangun == 3:
        volume = tabung()
        print("Volume tabung:", volume)
    else:
        print("Pilihan tidak valid.")
    print('=======================')
