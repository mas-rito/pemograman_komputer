def hitung_tunjangan(jumlah_anak, gaji_pokok):
    tunjangan = gaji_pokok * 15/100
    if jumlah_anak <= 3:
        tunjangan_anak = tunjangan * jumlah_anak

    return tunjangan_anak

print('Hitung tunjangan anak mu!')

gaji_pokok = int(input("Masukkan gaji pokok: "))
anak = int(input("Masukkan jumlah anak: "))
tunjangan = hitung_tunjangan(anak, gaji_pokok)
print('=======================')
print(f"Tunjangan anak: {int(tunjangan)}")