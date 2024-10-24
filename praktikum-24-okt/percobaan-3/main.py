# Buatlah program menghitung luas bangun datar dan volume bangun ruang (7 menu)
# dimana operasi hitung luas dan volumenya terpisah pada modul yang berbeda dan
# dipanggil pada program utama.

from luas_bangun_datar import luas_bangun_datar
from volume_bangun_ruang import volume_bangun_ruang

def menu():
    print("Menu Perhitungan Luas dan Volume")
    print("1. Hitung Luas Bangun Datar")
    print("2. Hitung Volume Bangun Ruang")
    print("3. Keluar")
    pilihan = int(input("Masukkan pilihan Anda: "))
    return pilihan

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
