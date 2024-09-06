print("Menghitung Detik")
detik = int(input('Masukan detik: '))

jam = detik//3600
menit = (detik%3600)//60
sisa_detik = (detik%3600)%60

print("----------------")
print("Hasil Perhitungan:")
print("----------------")
print(f"{jam} jam {menit} menit {sisa_detik} detik")