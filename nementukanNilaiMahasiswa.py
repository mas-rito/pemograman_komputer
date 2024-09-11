"""
Buatlah algoritma/flowchart uang membaca nilai mahasiswa dengan kategori: "A", "B","C"
dan dinyatakan lulus. Sedangkan kategori: "D","E" tidak lulus kuliah.
Serta tampilkan berapa banyak mahasiswa yang lulus dan tidak lulus
"""

# input jumlah nilai yang akan di input
jumlah_nilai = int(input("Masukkan Jumlah Nilai: "))

jumlah_lulus=0
jumlah_tidak_lulus=0

for i in range(jumlah_nilai):
    # input nilai mahasiswa: A,B,C,D,E
    nilai = input("Masukkan Nilai: ")
    # kondisi jika nilai mahasiswa sama dengan A atau B atau C maka nilai jumlah_lulus bertambah satu
    # jika nilai tidak sama dengan A,B,C maka nilai jumlah_tidak_lulus bertambah satu
    if nilai == "A" or nilai == "B" or nilai == "C" :
        jumlah_lulus += 1
    else :
        jumlah_tidak_lulus += 1

# output
print("Jumlah Mahasiswa Lulus: ", jumlah_lulus)
print("Jumlah Mahasiswa Tidak Lulus: ", jumlah_tidak_lulus)