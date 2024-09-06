def konversi_ke_detik(jam, menit, detik):
  total_detik = (jam * 3600) + (menit * 60) + detik
  return total_detik

print('Masukan Nilai:')
jam = int(input("Masukkan jumlah jam: "))
menit = int(input("Masukkan jumlah menit: "))
detik = int(input("Masukkan jumlah detik: "))


total_detik = konversi_ke_detik(jam, menit, detik)

print("----------------")
print("Hasil Perhitungan:")
print("----------------")
print("Total detik:", total_detik)