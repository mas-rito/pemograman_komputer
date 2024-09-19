
jumlah_lulus = 0
jumlah_tidak_lulus = 0

while True:
    print("Masukkan kategori nilai mahasiswa (A, B, C, D, E) atau 'selesai' untuk melihat hasil:")
    kategori_nilai = input("Masukkan kategori nilai mahasiswa: ")

    if kategori_nilai == "A" or kategori_nilai == "B" or kategori_nilai == "C":
        jumlah_lulus += 1
    elif kategori_nilai == "D" or kategori_nilai == "E":
        jumlah_tidak_lulus += 1
    elif kategori_nilai == "selesai":
        break
    else:
        print("Input tidak valid")
        break

print(f'Jumlah mahasiswa yang lulus: {jumlah_lulus} dan yang tidak lulus: {jumlah_tidak_lulus} dari {jumlah_lulus + jumlah_tidak_lulus} mahasiswa')