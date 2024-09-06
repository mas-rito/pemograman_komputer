def hitung_gaji_bersih(gaji_pokok):
  tunjangan = gaji_pokok * 20/100
  gaji_kotor = gaji_pokok + tunjangan
  pajak = gaji_kotor * 15/100
  gaji_bersih = gaji_kotor - pajak

  print(f"Gaji bersih karyawan: Rp {gaji_bersih:,}")

print("Menghitung Gaji Bersih")
gaji_pokok = int(input("Masukkan gaji pokok: Rp "))

print("----------------")
print("Gaji Karyawan")
print("----------------")
hitung_gaji_bersih(gaji_pokok)