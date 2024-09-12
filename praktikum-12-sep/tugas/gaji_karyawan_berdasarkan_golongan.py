nama = input("Masukkan nama: ")
golongan = input("Masukkan golongan: ")
jam_kerja = int(input("Masukkan lama kerja dalam seminggu: "))

list_golongan = {"A": 5000, "B": 6000, "C": 7500, "D": 9000}

gaji_pokok = list_golongan[golongan]
gaji_total = 0
    
if jam_kerja > 150:
    jam_lembur = jam_kerja - 150
    upah_per_jam = gaji_pokok / 150 
    upah_lembur_per_jam = upah_per_jam * 25/100
    upah_lembur = jam_lembur * upah_lembur_per_jam

    gaji_total = gaji_pokok * jam_kerja + upah_lembur
else:
    gaji_total = gaji_pokok * jam_kerja
    upah_lembur = 0
    
print("----------------")
print("Gaji Karyawan")
print("----------------")
print(f"Nama: {nama}")
print(f"Golongan: {golongan}")
print(f"Gaji total per minggu: Rp {gaji_total:,}")
