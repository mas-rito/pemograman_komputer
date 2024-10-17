def hitung_gaji(golongan, jam_kerja):
    gaji_lembur = 0

    if golongan == 1:
        upah_per_jam = 3000
    elif golongan == 2:
        upah_per_jam = 3500
    elif golongan == 3:
        upah_per_jam = 4000
    else:
        upah_per_jam = 5000

    if jam_kerja <= 40:
        gaji_pokok = jam_kerja * upah_per_jam
    else:
        gaji_pokok = 40 * upah_per_jam
        jam_lembur = jam_kerja - 40
        gaji_lembur = jam_lembur * upah_per_jam * 1.5

    gaji_total = gaji_pokok + gaji_lembur
    return gaji_total

print("Menghitung gaji karyawan")
golongan = int(input("Masukkan golongan karyawan (1, 2, 3, atau 4): "))
jam_kerja = float(input("Masukkan jumlah jam kerja dalam seminggu: "))

gaji = int(hitung_gaji(golongan, jam_kerja))
print('=======================')
print(f"Gaji mingguan karyawan: Rp {gaji:,}")